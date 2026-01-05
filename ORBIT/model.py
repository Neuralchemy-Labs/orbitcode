"""Simple model wrapper for Orbit"""
from llama_cpp import Llama
import yaml
from pathlib import Path
from typing import Iterator


class OrbitModel:
    """Lightweight model wrapper - loads once, reuses forever"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config = self._load_config(config_path)
        self._llm = None
    
    def _load_config(self, path: str) -> dict:
        """Load configuration from YAML"""
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def _detect_gpu(self) -> int:
        """Detect GPU availability and return optimal n_gpu_layers"""
        try:
            # Try to get GPU info from llama-cpp-python
            # If GPU is available, use a high number of layers
            # This is a simple heuristic - users can override in config
            import platform
            
            # Check if CUDA is available (NVIDIA GPUs)
            try:
                from llama_cpp import llama_cpp
                # If we can import and have GPU support compiled
                # Default to using all layers on GPU
                print("🟢 GPU detected! Will use GPU acceleration.")
                return 43  # Default for mid-range GPUs like RTX 3060
            except:
                print("🟡 No GPU detected. Using CPU only.")
                return 0  # CPU only
        except Exception as e:
            print(f"⚠️  GPU detection failed: {e}. Defaulting to config value.")
            return None  # Use config value
    
    def get_llm(self) -> Llama:
        """Lazy load - model loads only when first needed"""
        if self._llm is None:
            print("🔵 Loading model (one-time setup)...")
            
            model_config = self.config['model']
            perf_config = self.config['performance']
            
            model_path = model_config['path']
            if not Path(model_path).exists():
                raise FileNotFoundError(f"Model not found: {model_path}")
            
            # Auto-detect GPU if not explicitly set
            n_gpu_layers = perf_config.get('n_gpu_layers')
            if n_gpu_layers is None or n_gpu_layers == -1:  # -1 means auto-detect
                detected = self._detect_gpu()
                n_gpu_layers = detected if detected is not None else 0
            
            self._llm = Llama(
                model_path=model_path,
                n_ctx=perf_config['n_ctx'],
                n_threads=perf_config['n_threads'],
                n_batch=perf_config['n_batch'],
                n_gpu_layers=n_gpu_layers,
                verbose=False,
            )
            
            print(f"✅ {model_config['name']} ready!")
            print(f"⚙️  GPU Layers: {n_gpu_layers}\n")
        
        return self._llm
    
    def generate(self, prompt: str, stream: bool = True) -> Iterator[str]:
        """
        Generate response with streaming
        
        Args:
            prompt: Complete formatted prompt
            stream: Whether to stream tokens
            
        Yields:
            Generated tokens
        """
        llm = self.get_llm()
        gen_config = self.config['generation']
        
        response = llm(
            prompt,
            max_tokens=gen_config['max_tokens'],
            temperature=gen_config['temperature'],
            top_p=gen_config['top_p'],
            top_k=gen_config['top_k'],
            repeat_penalty=gen_config['repeat_penalty'],
            stream=stream,
            stop=["<|im_end|>", "\n\nUser:", "User:"],
        )
        
        if stream:
            for chunk in response:
                token = chunk["choices"][0]["text"]
                yield token
        else:
            yield response["choices"][0]["text"]
