"""Orbit - Offline Coding Assistant"""
from model import OrbitModel
from context import ContextManager
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from pathlib import Path


class Orbit:
    """Main Orbit CLI interface"""
    
    def __init__(self):
        self.console = Console()
        self.model = OrbitModel()
        self.context_mgr = ContextManager()
        
        # Setup prompt with history
        history_file = Path.home() / ".orbit_history"
        self.session = PromptSession(history=FileHistory(str(history_file)))
    
    def show_welcome(self):
        """Display welcome message"""
        welcome = """
# 🌍 Orbit - Offline Coding Assistant

**Context-aware coding with full privacy**

Commands:
- `/help` - Show this help
- `/context` - Show loaded context info
- `/clear` - Clear conversation history
- `/exit` - Exit Orbit

Just type your coding questions naturally!
        """
        self.console.print(Markdown(welcome))
        
        # Show context status
        ctx_info = self.context_mgr.get_context_info()
        status = "✅" if all([ctx_info['system'], ctx_info['project'], ctx_info['conventions']]) else "⚠️"
        self.console.print(f"\n{status} Context: System={ctx_info['system']}, Project={ctx_info['project']}, Conventions={ctx_info['conventions']}\n")
    
    def handle_command(self, cmd: str) -> bool:
        """
        Handle special commands
        
        Returns:
            True to continue, False to exit
        """
        cmd = cmd.strip().lower()
        
        if cmd == "/exit" or cmd == "/quit":
            self.console.print("[yellow]Goodbye! 👋[/yellow]")
            return False
        
        elif cmd == "/help":
            self.show_welcome()
        
        elif cmd == "/context":
            ctx_info = self.context_mgr.get_context_info()
            self.console.print("\n[cyan]Context Status:[/cyan]")
            self.console.print(f"  System Rules: {'✅' if ctx_info['system'] else '❌'}")
            self.console.print(f"  Project Info: {'✅' if ctx_info['project'] else '❌'}")
            self.console.print(f"  Conventions: {'✅' if ctx_info['conventions'] else '❌'}")
            self.console.print(f"  History: {ctx_info['history_length']} messages\n")
        
        elif cmd == "/clear":
            self.context_mgr.clear_history()
            self.console.print("[green]✓ Cleared conversation history[/green]")
        
        else:
            self.console.print(f"[red]Unknown command: {cmd}[/red]")
            self.console.print("Type /help for available commands")
        
        return True
    
    def chat_loop(self):
        """Main chat loop"""
        while True:
            try:
                # Get user input
                user_input = self.session.prompt("\n💬 You: ")
                
                if not user_input.strip():
                    continue
                
                # Handle commands
                if user_input.startswith("/"):
                    if not self.handle_command(user_input):
                        break
                    continue
                
                # Build prompt with context
                prompt = self.context_mgr.build_prompt(user_input)
                
                # Add to history
                self.context_mgr.add_to_history("user", user_input)
                
                # Generate response with streaming
                self.console.print("\n🤖 Orbit: ", end="", style="bold cyan")
                
                response_text = ""
                for token in self.model.generate(prompt, stream=True):
                    self.console.print(token, end="")
                    response_text += token
                
                self.console.print()  # Newline
                
                # Add response to history
                self.context_mgr.add_to_history("assistant", response_text)
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Use /exit to quit[/yellow]")
                continue
            except EOFError:
                break
            except Exception as e:
                self.console.print(f"\n[red]Error: {e}[/red]")
                continue
    
    def run(self):
        """Run Orbit"""
        self.console.clear()
        self.show_welcome()
        
        # Check if context files exist
        contexts_dir = Path("contexts")
        if not contexts_dir.exists():
            self.console.print("[yellow]⚠️  No contexts/ folder found. Creating example files...[/yellow]\n")
            self.create_example_contexts()
        
        # Start chat loop
        self.chat_loop()
    
    def create_example_contexts(self):
        """Create example context files"""
        contexts_dir = Path("contexts")
        contexts_dir.mkdir(exist_ok=True)
        
        # Create example files
        if not (contexts_dir / "system.txt").exists():
            (contexts_dir / "system.txt").write_text(
                "You are Orbit, an expert offline coding assistant.\n"
                "Provide clean, production-ready code.\n"
                "Follow the project conventions exactly.\n"
                "Be concise but thorough."
            )
        
        if not (contexts_dir / "project.txt").exists():
            (contexts_dir / "project.txt").write_text(
                "# Edit this file with your project details\n\n"
                "Project: [Your Project Name]\n"
                "Stack: [Your Tech Stack]\n"
                "Architecture: [Your Architecture]\n"
            )
        
        if not (contexts_dir / "conventions.txt").exists():
            (contexts_dir / "conventions.txt").write_text(
                "# Edit this file with your coding conventions\n\n"
                "- Use type hints\n"
                "- Write docstrings\n"
                "- Follow PEP 8\n"
            )
        
        self.console.print("[green]✓ Created example context files in contexts/[/green]")
        self.console.print("[cyan]Edit them to customize Orbit for your project![/cyan]\n")


def main():
    """Entry point"""
    orbit = Orbit()
    orbit.run()


if __name__ == "__main__":
    main()
