# Contributing to Orbit 🌍

First off, thank you for considering contributing to Orbit! It's people like you that make Orbit such a great tool for the developer community.

## 🎯 Philosophy

Orbit follows a **"Simple, Not Simplistic"** philosophy:
- Keep the codebase minimal and readable
- Plain text configuration over complex formats
- No unnecessary dependencies or abstractions
- Direct and efficient implementations

When contributing, please keep this philosophy in mind.

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**
```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Run '....'
3. See error

**Expected behavior**
What you expected to happen.

**Environment:**
- OS: [e.g. Windows 11, Ubuntu 22.04]
- GPU: [e.g. RTX 3060 12GB]
- Python Version: [e.g. 3.10.5]
- Model: [e.g. Qwen2.5-Coder-7B Q5_K_M]

**Additional context**
Add any other context about the problem here.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Clear title and description** of the enhancement
- **Use case**: Why is this enhancement useful?
- **Proposed solution**: How would you implement it?
- **Alternatives considered**: What other solutions did you think about?

### Pull Requests

We actively welcome your pull requests! Here's the process:

1. **Fork the repo** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

## 📝 Development Setup

### 1. Clone Your Fork

```bash
git clone https://github.com/your-username/orbit.git
cd orbit
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download a Test Model

```bash
mkdir models
cd models
huggingface-cli download Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF qwen2.5-coder-1.5b-instruct-q4_k_m.gguf --local-dir . --local-dir-use-symlinks False
```

### 5. Run Tests

```bash
# CLI Mode
python orbit.py

# Web UI Mode
python orbit_web.py
```

## 🎨 Code Style Guidelines

### Python Code Standards

- **Follow PEP 8** style guide
- **Type hints**: Use type hints for all function signatures
- **Docstrings**: Use Google-style docstrings for all public functions
- **Line length**: Maximum 100 characters
- **Imports**: Group imports (standard library, third-party, local)

**Example:**

```python
def generate_response(
    prompt: str,
    temperature: float = 0.7,
    max_tokens: int = 2048
) -> str:
    """Generate a response from the LLM.
    
    Args:
        prompt: The input prompt to generate from
        temperature: Sampling temperature (0.0 to 1.0)
        max_tokens: Maximum number of tokens to generate
        
    Returns:
        Generated response text
        
    Raises:
        ValueError: If temperature is out of range
    """
    # Implementation here
    pass
```

### File Organization

- Keep files focused and single-purpose
- Maximum ~300 lines per file (split if needed)
- Clear separation of concerns

### Documentation

- Update README.md if adding user-facing features
- Add docstrings to all new functions
- Comment complex logic, but prefer self-documenting code

## 🔍 What We're Looking For

### High Priority Contributions

- 🐛 **Bug fixes** - Always welcome!
- 📖 **Documentation improvements** - Make it clearer!
- 🎨 **UI/UX enhancements** - Better user experience
- ⚡ **Performance optimizations** - Faster is better
- 🧪 **Test coverage** - Help us test more scenarios

### Feature Contributions

When adding features, consider:

1. **Does it align with Orbit's philosophy?** (Simple, offline, privacy-first)
2. **Is it generally useful?** (Not too specific to one use case)
3. **Does it add complexity?** (Keep it minimal)
4. **Is it well-documented?** (README, docstrings, examples)

### Ideas for Contributions

Here are some areas where contributions are especially welcome:

- **Model support**: Test and document new GGUF models
- **Templates**: Add useful prompt templates for common tasks
- **Performance**: Optimize inference speed or memory usage
- **Cross-platform**: Test and fix issues on different OS/hardware
- **Documentation**: Tutorials, examples, better explanations
- **Accessibility**: Make Orbit easier to use for everyone

## 🚫 What to Avoid

Please don't:

- Add heavy dependencies without strong justification
- Break backward compatibility without discussion
- Add features that require internet connectivity
- Over-engineer simple solutions
- Submit PRs without testing

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Self-review of your own code
- [ ] Comments added for complex logic
- [ ] Documentation updated (if needed)
- [ ] No new warnings or errors
- [ ] Tested on your local machine
- [ ] Commit messages are clear and descriptive

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran and your testing environment.

## Checklist:
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

## 🌟 Recognition

Contributors will be recognized in:
- GitHub contributors list
- Future changelog entries
- Hall of fame in README (for significant contributions)

## 📞 Getting Help

- **Questions?** Open a GitHub Discussion
- **Bugs?** Open an issue with the bug template
- **Ideas?** Open an issue with the enhancement template

## 📜 Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior by opening an issue.

## 🎉 Thank You!

Your contributions, whether big or small, make Orbit better for everyone. We appreciate your time and effort!

---

**Happy Coding! 🚀**
