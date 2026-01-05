"""Orbit Web UI - Simple Chat Interface"""
import gradio as gr
from model import OrbitModel
from context import ContextManager


# Initialize
model = OrbitModel()
context_manager = ContextManager()


def respond(message, history, template_choice, use_project_context):
    """Generate response with streaming"""
    # Set template
    if template_choice != "None":
        context_manager.load_template(template_choice)
    else:
        context_manager.current_template = None
    
    # Build prompt
    override = not use_project_context
    prompt = context_manager.build_prompt(message, override_project_context=override)
    
    # Generate with streaming
    response = ""
    for token in model.generate(prompt, stream=True):
        response += token
        yield response
    
    # Save to history
    context_manager.add_to_history("user", message)
    context_manager.add_to_history("assistant", response)


# Build UI  
with gr.Blocks(title="Orbit - Offline Coding Assistant") as app:
    
    gr.Markdown("# 🌍 Orbit - Offline Coding Assistant")
    gr.Markdown("**Context-aware code generation • 100% offline • Privacy-first**")
    
    # Settings Row
    with gr.Row():
        template = gr.Dropdown(
            choices=["None"] + context_manager.list_templates(),
            value="None",
            label="Template",
            scale=2
        )
        use_context = gr.Checkbox(
            value=True,
            label="Use Project Context",
            scale=1
        )
    
    # Chat Interface (Gradio 6.x compatible - no retry_btn, undo_btn, or clear_btn)
    chat_interface = gr.ChatInterface(
        fn=respond,
        additional_inputs=[template, use_context],
        chatbot=gr.Chatbot(height=550),
        textbox=gr.Textbox(
            placeholder="Ask anything... (e.g., 'Create a FastAPI login endpoint')",
            container=False
        )
    )
    
    gr.Markdown("---\n🔒 **Privacy First** • Your code never leaves your machine")


if __name__ == "__main__":
    print("🌍 Orbit - Starting...")
    print("🌐 Opening at: http://127.0.0.1:7860\n")
    
    app.launch(
        server_name="127.0.0.1",
        server_port=7860,
        inbrowser=True,
        theme=gr.themes.Soft()  # Theme parameter goes in launch() for Gradio 6.x
    )