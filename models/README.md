# Orbit Model Setup Guide

## Recommended Models

Orbit works with any GGUF format model compatible with llama-cpp-python. Here are our tested recommendations:

### 🥇 **Best for RTX 3060 (12GB VRAM)**

#### Qwen2.5-Coder-14B-Instruct (Recommended)
- **Size:** ~8.5GB (Q5_K_M quantization)
- **VRAM:** ~10GB
- **Performance:** Excellent code quality, fast inference
- **Download:** [TheBloke/Qwen2.5-Coder-14B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-GGUF)

```bash
# Download with HuggingFace CLI
huggingface-cli download Qwen/Qwen2.5-Coder-14B-Instruct-GGUF \
  qwen2.5-coder-14b-instruct-q5_k_m.gguf \
  --local-dir ./models
```

### 🥈 **Alternative Models**

#### DeepSeek-Coder-6.7B
- **Size:** ~4GB (Q5_K_M)
- **VRAM:** ~5GB
- **Best for:** Lighter workloads, faster responses
- **Download:** [TheBloke/deepseek-coder-6.7b-instruct-GGUF](https://huggingface.co/TheBloke/deepseek-coder-6.7b-instruct-GGUF)

#### CodeLlama-13B-Instruct
- **Size:** ~7GB (Q4_K_M)
- **VRAM:** ~8GB
- **Best for:** General code generation
- **Download:** [TheBloke/CodeLlama-13B-Instruct-GGUF](https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF)

---

## GPU Memory Requirements

| Model Size | Quantization | VRAM Needed | Best GPU |
|------------|--------------|-------------|-----------|
| 7B | Q4_K_M | 4-5GB | RTX 3060, RTX 2060 |
| 7B | Q5_K_M | 5-6GB | RTX 3060, RTX 3070 |
| 14B | Q4_K_M | 8-9GB | RTX 3060 (12GB) |
| 14B | Q5_K_M | 10-11GB | RTX 3060 (12GB), RTX 3080 |
| 32B | Q4_K_M | 18-20GB | RTX 3090, RTX 4090 |

---

## Installation Steps

### Option 1: Manual Download (Recommended)

1. **Visit HuggingFace:**
   - Go to the model page (links above)
   - Click on "Files and versions"
   - Download the `.gguf` file

2. **Place in models folder:**
   ```
   orbit/
   └── models/
       └── qwen2.5-coder-14b-instruct-q5_k_m.gguf
   ```

3. **Update config.yaml:**
   ```yaml
   model:
     path: "models/qwen2.5-coder-14b-instruct-q5_k_m.gguf"
     name: "Qwen2.5-Coder-14B"
   ```

### Option 2: HuggingFace CLI

1. **Install HuggingFace CLI:**
   ```bash
   pip install huggingface-hub
   ```

2. **Download model:**
   ```bash
   # Create models directory
   mkdir models
   
   # Download Qwen2.5-Coder-14B
   huggingface-cli download Qwen/Qwen2.5-Coder-14B-Instruct-GGUF \
     qwen2.5-coder-14b-instruct-q5_k_m.gguf \
     --local-dir ./models
   ```

3. **Update config** as shown above

---

## Quantization Guide

**What is quantization?** Compression technique to reduce model size and memory usage.

| Quantization | Quality | Size | Speed | Recommendation |
|--------------|---------|------|-------|----------------|
| Q4_K_M | Good | Small | Fast | Budget GPUs (6-8GB VRAM) |
| Q5_K_M | Better | Medium | Medium | **Recommended** (8-12GB VRAM) |
| Q6_K | Best | Large | Slower | High-end GPUs (16GB+ VRAM) |
| Q8_0 | Excellent | Largest | Slowest | Overkill for most use cases |

**For RTX 3060:** Use Q5_K_M - best balance of quality and performance.

---

## Troubleshooting

### "Model not found" error
- Check the path in `config.yaml` is correct
- Ensure the `.gguf` file is in the `models/` folder
- Use absolute path if needed: `E:/ORBIT/models/model.gguf`

### Out of memory error
- Use smaller model (7B instead of 14B)
- Use lighter quantization (Q4 instead of Q5)
- Reduce `n_ctx` in config.yaml (8192 → 4096)
- Lower `n_gpu_layers` in config.yaml

### Slow generation
- Increase `n_gpu_layers` (use more GPU)
- Increase `n_batch` (512 → 1024)
- Use smaller context window (`n_ctx`)

---

## Performance Tips

1. **First run is slower** - Model loads into GPU memory
2. **Context is cached** - Follow-up queries are faster
3. **More GPU layers = faster** - But uses more VRAM
4. **Streaming is instant** - You see tokens immediately

---

**Need help?** The models folder is already created for you. Just download a model and update the config!
