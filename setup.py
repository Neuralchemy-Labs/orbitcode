#!/usr/bin/env python3
"""
Orbit Setup Script
Quick setup wizard for new users
"""
import os
import shutil
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")


def print_success(text):
    """Print success message"""
    print(f"✅ {text}")


def print_info(text):
    """Print info message"""
    print(f"ℹ️  {text}")


def check_context_files():
    """Check and setup context files"""
    print_header("Setting Up Context Files")
    
    contexts_dir = Path("contexts")
    
    # Check if user already has context files
    has_project = (contexts_dir / "project.txt").exists()
    has_conventions = (contexts_dir / "conventions.txt").exists()
    
    if has_project and has_conventions:
        print_success("Context files already exist!")
        return
    
    # Copy example files if needed
    if not has_project and (contexts_dir / "project.txt.example").exists():
        print_info("Creating project.txt from example...")
        shutil.copy(
            contexts_dir / "project.txt.example",
            contexts_dir / "project.txt"
        )
        print_success("Created contexts/project.txt")
        print("   👉 Edit this file to describe your project!")
    
    if not has_conventions and (contexts_dir / "conventions.txt.example").exists():
        print_info("Creating conventions.txt from example...")
        shutil.copy(
            contexts_dir / "conventions.txt.example",
            contexts_dir / "conventions.txt"
        )
        print_success("Created contexts/conventions.txt")
        print("   👉 Edit this file to set your coding conventions!")


def check_model():
    """Check if a model is downloaded"""
    print_header("Checking Model")
    
    models_dir = Path("models")
    gguf_files = list(models_dir.glob("*.gguf"))
    
    if gguf_files:
        print_success(f"Found model: {gguf_files[0].name}")
        return True
    else:
        print("⚠️  No model found!")
        print("\n📥 Download a model:")
        print("   See README.md for model recommendations based on your GPU")
        print("\n   Quick start (RTX 3060):")
        print("   ```")
        print("   huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF \\")
        print("       qwen2.5-coder-7b-instruct-q5_k_m.gguf \\")
        print("       --local-dir models --local-dir-use-symlinks False")
        print("   ```")
        return False


def check_config():
    """Check config.yaml"""
    print_header("Checking Configuration")
    
    config_file = Path("config.yaml")
    if config_file.exists():
        print_success("config.yaml exists")
        print("   👉 Update the model path if needed!")
        return True
    else:
        print("⚠️  config.yaml not found!")
        return False


def print_next_steps(has_model):
    """Print next steps"""
    print_header("🎉 Setup Complete!")
    
    if has_model:
        print("You're ready to use Orbit!\n")
        print("🚀 Start Orbit:")
        print("   CLI:    python orbit.py")
        print("   Web UI: python orbit_web.py\n")
    else:
        print("⚠️  Almost ready! You need to:\n")
        print("1. Download a model (see above)")
        print("2. Update config.yaml with the model path")
        print("3. Run: python orbit_web.py\n")
    
    print("📝 Don't forget to:")
    print("   - Edit contexts/project.txt (your project info)")
    print("   - Edit contexts/conventions.txt (your coding style)")
    print("\n📖 For more help, see README.md")


def main():
    """Main setup function"""
    print_header("🌍 Welcome to Orbit Setup!")
    print("This wizard will help you get started.\n")
    
    # Check dependencies
    try:
        import yaml
        import gradio
        from llama_cpp import Llama
        print_success("All dependencies installed")
    except ImportError as e:
        print(f"⚠️  Missing dependency: {e}")
        print("\n📦 Install dependencies:")
        print("   pip install -r requirements.txt")
        return
    
    # Setup context files
    check_context_files()
    
    # Check model
    has_model = check_model()
    
    # Check config
    check_config()
    
    # Print next steps
    print_next_steps(has_model)


if __name__ == "__main__":
    main()
