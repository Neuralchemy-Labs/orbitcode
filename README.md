# OrbitCode

⚠️ **EXPERIMENTAL - Work in Progress**

AI coding assistant experiment using open-source models.

**Status:** Early development • Exploring viability • Not production-ready

## Concept

Unlimited AI coding assistance using local/open-source models:
- No API costs
- Privacy-first
- Customizable

## Current State

~50% complete. Exploring whether small models (14B) can provide useful coding assistance.

**Known limitations:**
- Basic functionality only
- Limited model performance
- Needs significant polish

## Why This Exists

Experimenting with feasibility of cost-free AI coding tools. May continue development based on results.

---

**This is a learning project in Neural Alchemy Labs.**
**Context-aware coding with full privacy. Your code, your machine, your control.**

> ℹ️ **Note**  
> This project explores system design and implementation patterns using AI-assisted development. It prioritizes clarity of architecture and ideas over production guarantees.

Orbit is a fully offline coding assistant designed for developers who value privacy, control, and context-aware code generation.

## 🚀 Why Orbit?

**The Problem:**
- Copy-pasting project context into ChatGPT/Claude every time
- Your code going to the cloud
- Generic code that doesn't match your style
- Losing context between sessions

**The Solution:**
- Define your project context **once**
- Get code that follows **your** conventions
- Everything runs **offline** on your machine
- Context persists across all sessions

## ✨ Features

✅ **100% Offline** - No cloud, no APIs, no internet required  
✅ **Context-Aware** - Remembers your project, stack, and conventions  
✅ **Privacy-First** - Your code never leaves your machine  
✅ **Web UI & CLI** - Beautiful web interface or terminal  
✅ **Prompt Templates** - Pre-made templates for common tasks  
✅ **Auto GPU Detection** - Automatically uses your GPU  
✅ **Streaming Responses** - See tokens as they generate  
✅ **Simple Setup** - 4 files, plain text contexts  

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/orbit.git
cd orbit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** For GPU acceleration on Windows with NVIDIA GPUs, install the CUDA version:
> ```bash
> pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124
> ```

### 3. Download a Model

See [Model Selection Guide](#-model-selection-guide) below for recommendations based on your GPU.

---

## 🤖 Model Selection Guide

### **GPU-Based Recommendations**

| GPU | VRAM | Recommended Model | Quantization | File Size | Download Command |
|-----|------|------------------|--------------|-----------|------------------|
| **RTX 3060** | 12GB | Qwen2.5-Coder-7B | Q5_K_M | ~5.5GB | See below |
| **RTX 3070/3080** | 8-10GB | Qwen2.5-Coder-7B | Q8_0 | ~7.5GB | See below |
| **RTX 4090** | 24GB | Qwen2.5-Coder-32B | Q5_K_M | ~21GB | See below |
| **RTX 4080** | 16GB | Qwen2.5-Coder-14B | Q5_K_M | ~10GB | See below |
| **CPU Only** | N/A | Qwen2.5-Coder-1.5B | Q4_K_M | ~1GB | See below |

### **Quantization Explained**

- **Q8_0**: Highest quality, largest size (~same as original)
- **Q5_K_M**: Best balance - high quality, reasonable size ⭐ **RECOMMENDED**
- **Q4_K_M**: Good quality, smaller size (fast inference)
- **Q3_K_M**: Lower quality, much smaller (use only if VRAM limited)
- **Q2_K**: Lowest quality, smallest size (not recommended)

> **Rule of Thumb:** Choose a model that's **1-2GB smaller** than your available VRAM for optimal performance.

---

## 📥 Model Download Links

### **Qwen2.5-Coder Models** (Recommended)

#### **Qwen2.5-Coder-7B-Instruct** ⭐ Best for RTX 3060/3070

**Direct Downloads:**
- [Q4_K_M (4.3GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/qwen2.5-coder-7b-instruct-q4_k_m.gguf)
- [Q5_K_M (5.2GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/qwen2.5-coder-7b-instruct-q5_k_m.gguf) ⭐ **RECOMMENDED**
- [Q8_0 (7.6GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/qwen2.5-coder-7b-instruct-q8_0.gguf)

**CLI Download:**
```bash
# Create models directory
mkdir models
cd models

# Download Q5_K_M (Recommended)
huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF qwen2.5-coder-7b-instruct-q5_k_m.gguf --local-dir . --local-dir-use-symlinks False

# OR download Q4_K_M (Faster, slightly lower quality)
huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF qwen2.5-coder-7b-instruct-q4_k_m.gguf --local-dir . --local-dir-use-symlinks False
```

---

#### **Qwen2.5-Coder-14B-Instruct** - Best for RTX 4070/4080

**Direct Downloads:**
- [Q4_K_M (8.5GB)](https://huggingface.co/bartowski/Qwen2.5-Coder-14B-Instruct-GGUF/resolve/main/Qwen2.5-Coder-14B-Instruct-Q4_K_M.gguf)
- [Q5_K_M (10.3GB)](https://huggingface.co/bartowski/Qwen2.5-Coder-14B-Instruct-GGUF/resolve/main/Qwen2.5-Coder-14B-Instruct-Q5_K_M.gguf) ⭐ **RECOMMENDED**
- [Q8_0 (15.2GB)](https://huggingface.co/bartowski/Qwen2.5-Coder-14B-Instruct-GGUF/resolve/main/Qwen2.5-Coder-14B-Instruct-Q8_0.gguf)

**CLI Download:**
```bash
mkdir models
cd models

# Download Q5_K_M (Recommended)
huggingface-cli download bartowski/Qwen2.5-Coder-14B-Instruct-GGUF Qwen2.5-Coder-14B-Instruct-Q5_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

---

#### **Qwen2.5-Coder-32B-Instruct** - Best for RTX 4090

**Direct Downloads:**
- [Q4_K_M (18.5GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct-GGUF/resolve/main/qwen2.5-coder-32b-instruct-q4_k_m-00001-of-00002.gguf)
- [Q5_K_M (22GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct-GGUF/resolve/main/qwen2.5-coder-32b-instruct-q5_k_m-00001-of-00002.gguf) ⭐ **RECOMMENDED**

> **Note:** 32B models may be split into multiple files. The CLI command below downloads all parts automatically.

**CLI Download:**
```bash
mkdir models
cd models

# Download Q5_K_M (Downloads all parts)
huggingface-cli download Qwen/Qwen2.5-Coder-32B-Instruct-GGUF --include "qwen2.5-coder-32b-instruct-q5_k_m*.gguf" --local-dir . --local-dir-use-symlinks False
```

---

#### **Qwen2.5-Coder-1.5B-Instruct** - Best for CPU-Only or Low VRAM

**Direct Downloads:**
- [Q4_K_M (1GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/resolve/main/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf) ⭐ **RECOMMENDED**
- [Q5_K_M (1.2GB)](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF/resolve/main/qwen2.5-coder-1.5b-instruct-q5_k_m.gguf)

**CLI Download:**
```bash
mkdir models
cd models

huggingface-cli download Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF qwen2.5-coder-1.5b-instruct-q4_k_m.gguf --local-dir . --local-dir-use-symlinks False
```

---

### **DeepSeek-Coder Models** (Alternative)

#### **DeepSeek-Coder-6.7B-Instruct**

**Direct Downloads:**
- [Q4_K_M (4.1GB)](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q4_K_M.gguf)
- [Q5_K_M (4.8GB)](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q5_K_M.gguf)

**CLI Download:**
```bash
mkdir models
cd models

huggingface-cli download TheBloke/deepseek-coder-6.7B-instruct-GGUF deepseek-coder-6.7b-instruct.Q5_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

---

### **CodeLlama Models** (Alternative)

#### **CodeLlama-13B-Instruct**

**Direct Downloads:**
- [Q4_K_M (7.9GB)](https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF/resolve/main/codellama-13b-instruct.Q4_K_M.gguf)
- [Q5_K_M (9GB)](https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF/resolve/main/codellama-13b-instruct.Q5_K_M.gguf)

**CLI Download:**
```bash
mkdir models
cd models

huggingface-cli download TheBloke/CodeLlama-13B-Instruct-GGUF codellama-13b-instruct.Q5_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

---

### **Quick Download Using Hugging Face CLI**

Install the Hugging Face CLI if you don't have it:
```bash
pip install -U huggingface_hub
```

Then use any of the download commands above. Models will be saved to the `models/` directory.

---

## ⚙️ Configuration

### 1. Update `config.yaml`

After downloading a model, update the path in `config.yaml`:

```yaml
model:
  path: "models/qwen2.5-coder-7b-instruct-q5_k_m.gguf"  # Update this
  name: "Qwen2.5-Coder-7B"

performance:
  n_ctx: 8192              # Context window size
  n_gpu_layers: 35         # GPU layers (adjust based on your GPU)
  n_threads: 6             # CPU threads
  n_batch: 512             # Batch size
```

### 2. GPU Layer Configuration

Adjust `n_gpu_layers` based on your GPU:

| GPU | VRAM | Recommended `n_gpu_layers` |
|-----|------|---------------------------|
| RTX 3060 (12GB) | 12GB | 35-40 |
| RTX 3070 (8GB) | 8GB | 30-35 |
| RTX 4070 (12GB) | 12GB | 40-45 |
| RTX 4080 (16GB) | 16GB | All layers (set to 99) |
| RTX 4090 (24GB) | 24GB | All layers (set to 99) |
| CPU Only | N/A | 0 |

> **Tip:** Start with the recommended value. If you experience crashes, reduce by 5-10. If you have VRAM to spare, increase gradually.

---

## 📝 Context Setup

### Customize Your Context Files

Edit the files in `contexts/` to make Orbit understand your project:

#### `contexts/system.txt`
```
You are a senior software engineer and coding assistant.
Generate production-ready, well-documented code.
Follow best practices and design patterns.
Explain your reasoning when making architectural decisions.
```

#### `contexts/project.txt`
```
Project: E-commerce API
Stack: FastAPI, PostgreSQL, SQLAlchemy, Redis
Architecture: Clean Architecture with DDD
Auth: JWT tokens with refresh mechanism
Testing: pytest, 80%+ coverage required
Deployment: Docker, Kubernetes
```

#### `contexts/conventions.txt`
```
- Use type hints for all function signatures
- Maximum line length: 100 characters
- Use Pydantic for data validation
- Follow PEP 8 style guide
- Write docstrings in Google style
- Use dependency injection pattern
```

Orbit reads these files and includes them in **every** request for consistent, context-aware code generation.

---

## 🚀 Usage

### **Web UI** (Recommended)

1. Start the web interface:
```bash
python orbit_web.py
```

2. Open your browser at `http://127.0.0.1:7860`

3. Features:
   - 🎨 Beautiful syntax highlighting
   - 📋 One-click copy button
   - 🔄 Real-time streaming
   - 📝 Template selector
   - 🔒 100% offline

![Orbit Web UI](https://via.placeholder.com/800x400?text=Orbit+Web+UI)

---

### **CLI Mode**

```bash
python orbit.py
```

**Example Session:**
```
💬 You: Create a FastAPI endpoint for user login

🤖 Orbit: [Generates code following YOUR conventions and stack]

💬 You: Add rate limiting to prevent brute force

🤖 Orbit: [Updates the code with rate limiting using your project's stack]
```

**Commands:**

| Command | Description |
|---------|-------------|
| `/help` | Show help |
| `/context` | Show loaded context info |
| `/clear` | Clear conversation history |
| `/exit` | Exit Orbit |

---

## 📂 Project Structure

```
orbit/
├── orbit.py              # CLI interface
├── orbit_web.py          # Web UI (Gradio)
├── model.py              # Model wrapper
├── context.py            # Context manager
├── config.yaml           # Configuration settings
├── requirements.txt      # Python dependencies
├── contexts/             # Your context files
│   ├── system.txt        # AI behavior rules
│   ├── project.txt       # Your project info
│   └── conventions.txt   # Your coding style
├── templates/            # Prompt templates
│   ├── code_generation.txt
│   ├── code_review.txt
│   ├── refactor.txt
│   ├── bug_fix.txt
│   └── documentation.txt
└── models/               # Your GGUF models
    ├── README.md
    └── [your-model].gguf
```

---

## 🎯 Prompt Templates

Orbit includes **5 pre-made templates** for common coding tasks:

1. **Code Generation** - Clean, production-ready code
2. **Code Review** - Comprehensive code analysis
3. **Refactoring** - Improve code quality
4. **Bug Fix** - Identify and fix bugs
5. **Documentation** - Generate comprehensive docs

**Add your own:** Just create a `.txt` file in the `templates/` folder!

Example template (`templates/api_endpoint.txt`):
```
Task: Create a RESTful API endpoint

Requirements:
- Follow REST conventions
- Add input validation
- Include error handling
- Add logging
- Write unit tests
```

---

## 🔧 Performance Tuning

### For Faster Responses

Edit `config.yaml`:

```yaml
performance:
  n_ctx: 4096              # Reduce from 8192 (smaller context = faster)
  n_gpu_layers: 43         # Increase (more GPU, less CPU)
  n_threads: 4             # Reduce (let GPU do the work)
  n_batch: 1024            # Increase (bigger batches)

generation:
  temperature: 0.5         # Reduce from 0.7 (less sampling = faster)
  max_tokens: 1024         # Reduce from 4096 (shorter responses)
  top_k: 20                # Reduce from 40 (faster sampling)
```

### Typical Performance (RTX 3060, Qwen2.5-Coder-7B Q5_K_M)

- **First load:** ~5-10 seconds (model loading)
- **First query:** ~5-7 seconds (includes context processing)
- **Follow-up queries:** ~3-5 seconds (context cached)
- **Generation speed:** ~20-30 tokens/sec

> **Note:** Context is cached by llama.cpp, so subsequent queries are significantly faster!

---

## ❓ FAQ

**Q: Will large context slow down responses?**  
A: First query: slightly slower. Follow-up queries: cached by llama.cpp, fast as normal.

**Q: How much context can I add?**  
A: Recommended: 2-4K tokens total. Models support 8K-128K depending on the model.

**Q: Can I use multiple projects?**  
A: Yes! Create different context folders and swap them via `config.yaml`.

**Q: Does this work completely offline?**  
A: 100% offline. No internet connection needed after downloading the model.

**Q: My model is slow/crashing. What do I do?**  
A: Reduce `n_gpu_layers` by 5-10, or try a smaller quantization (Q4_K_M instead of Q5_K_M).

**Q: Can I use this with VS Code?**  
A: Currently CLI/Web UI only. VS Code extension is on the roadmap!

---

## 🗺️ Roadmap

- [ ] Context compression for very large projects
- [ ] Multiple context profiles (switch projects easily)
- [ ] VS Code extension
- [ ] File context loading (`/load file.py`)
- [ ] Code-only output mode
- [ ] Multi-model support (load multiple models)
- [ ] RAG integration for codebase search

---

## 🎨 Philosophy

**Simple, Not Simplistic**
- 4 core Python files
- Plain text contexts (no fancy formats)
- Direct llama-cpp-python (no HTTP overhead)
- Edit contexts with any text editor

**Context Over Prompts**
- Better context = better code
- Write context once, use forever
- Consistent, project-aware results

**Privacy & Control**
- Your code stays on your machine
- No telemetry, no tracking
- You own the AI, the code, everything

---

## 🤝 Contributing

Orbit is intentionally simple. PRs welcome, but must maintain the simplicity philosophy.

**Guidelines:**
- Keep it simple and focused
- No unnecessary dependencies
- Maintain plain text configuration
- Document all changes

---

## 📄 License

MIT License - Use freely, modify as needed.

---

## 🙏 Acknowledgments

- **llama.cpp** - Efficient LLM inference
- **Gradio** - Beautiful web interfaces
- **Qwen Team** - Excellent coding models
- **All contributors** to the open-source LLM ecosystem

---

**Built for developers who value privacy, control, and consistent code generation.**

⭐ **Star this repo if Orbit helps your workflow!**

