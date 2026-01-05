"""Simple context manager for Orbit"""
from pathlib import Path
from typing import List, Dict
import yaml


class ContextManager:
    """Loads and manages project context - simple text file based"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config = self._load_config(config_path)
        self.contexts_dir = Path("contexts")
        self.templates_dir = Path("templates")
        self.conversation_history: List[Dict[str, str]] = []
        self.current_template: str = None
    
    def _load_config(self, path: str) -> dict:
        """Load configuration"""
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def list_templates(self) -> List[str]:
        """List all available templates"""
        if not self.templates_dir.exists():
            return []
        
        templates = []
        for template_file in self.templates_dir.glob("*.txt"):
            # Convert filename to display name (e.g., code_generation.txt -> Code Generation)
            name = template_file.stem.replace('_', ' ').title()
            templates.append(name)
        return templates
    
    def load_template(self, template_name: str) -> str:
        """Load a specific template"""
        # Convert display name to filename (e.g., Code Generation -> code_generation.txt)
        filename = template_name.lower().replace(' ', '_') + '.txt'
        template_file = self.templates_dir / filename
        
        if template_file.exists():
            self.current_template = template_name
            return template_file.read_text()
        return None
    
    def load_context_files(self, override_project_context: bool = False) -> str:
        """Load all enabled context files
        
        Args:
            override_project_context: If True, skip loading project.txt for this request
        """
        context_config = self.config['context']
        context_parts = []
        
        # Load system rules
        if context_config['load_system']:
            system_file = self.contexts_dir / "system.txt"
            if system_file.exists():
                context_parts.append(f"# SYSTEM RULES\n{system_file.read_text()}")
        
        # Load project info (unless overridden)
        if context_config['load_project'] and not override_project_context:
            project_file = self.contexts_dir / "project.txt"
            if project_file.exists():
                context_parts.append(f"\n# PROJECT INFO\n{project_file.read_text()}")
        
        # Load coding conventions
        if context_config['load_conventions']:
            conventions_file = self.contexts_dir / "conventions.txt"
            if conventions_file.exists():
                context_parts.append(f"\n# CODING CONVENTIONS\n{conventions_file.read_text()}")
        
        # Load current template if set
        if self.current_template:
            template_content = self.load_template(self.current_template)
            if template_content:
                context_parts.append(f"\n# TEMPLATE: {self.current_template}\n{template_content}")
        
        return "\n".join(context_parts)
    
    def add_to_history(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})
        
        # Keep only recent history
        max_history = self.config['context']['max_history']
        if len(self.conversation_history) > max_history * 2:  # *2 for user+assistant pairs
            self.conversation_history = self.conversation_history[-(max_history * 2):]
    
    def build_prompt(self, user_message: str, override_project_context: bool = False) -> str:
        """
        Build complete prompt with context + history + new message
        
        Args:
            user_message: The user's input message
            override_project_context: If True, skip project context for this request
        
        Format: Qwen2.5 ChatML style
        """
        # Load static context (project rules, conventions)
        static_context = self.load_context_files(override_project_context)
        
        # Start with system message including context
        prompt = f"<|im_start|>system\n{static_context}<|im_end|>\n"
        
        # Add conversation history
        for msg in self.conversation_history:
            prompt += f"<|im_start|>{msg['role']}\n{msg['content']}<|im_end|>\n"
        
        # Add current user message
        prompt += f"<|im_start|>user\n{user_message}<|im_end|>\n"
        
        # Prepare for assistant response
        prompt += "<|im_start|>assistant\n"
        
        return prompt
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history.clear()
    
    def get_context_info(self) -> dict:
        """Get info about loaded contexts"""
        return {
            "system": (self.contexts_dir / "system.txt").exists(),
            "project": (self.contexts_dir / "project.txt").exists(),
            "conventions": (self.contexts_dir / "conventions.txt").exists(),
            "history_length": len(self.conversation_history),
        }
