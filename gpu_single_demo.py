#!/usr/bin/env python3
import time
import os
from datetime import datetime

def check_gpu():
    """Check for GPU availability"""
    try:
        import torch
        if torch.cuda.is_available():
            return True, torch.cuda.get_device_name(0), torch.cuda.device_count()
        return False, None, 0
    except ImportError:
        return False, "PyTorch not available", 0

def gpu_computation():
    """Simple GPU computation if available"""
    try:
        import torch
        if torch.cuda.is_available():
            # Simple matrix multiplication on GPU
            device = torch.device('cuda')
            a = torch.randn(1000, 1000, device=device)
            b = torch.randn(1000, 1000, device=device)
            result = torch.mm(a, b)
            return result.sum().item()
        return None
    except ImportError:
        return None

def main():
    print(f"=== GPU Single Job Demo ===")
    print(f"Start time: {datetime.now()}")
    print(f"CUDA_VISIBLE_DEVICES: {os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set')}")
    
    gpu_available, gpu_name, gpu_count = check_gpu()
    print(f"GPU Available: {gpu_available}")
    if gpu_available:
        print(f"GPU Name: {gpu_name}")
        print(f"GPU Count: {gpu_count}")
        
        print("Running GPU computation...")
        start = time.time()
        result = gpu_computation()
        end = time.time()
        
        print(f"GPU computation result: {result}")
        print(f"Computation time: {end - start:.2f} seconds")
    else:
        print("No GPU available, running CPU fallback...")
        start = time.time()
        result = sum(i**2 for i in range(100000))
        end = time.time()
        print(f"CPU result: {result}")
        print(f"Computation time: {end - start:.2f} seconds")
    
    print(f"End time: {datetime.now()}")
    print("=== GPU Single Job Complete ===")

if __name__ == "__main__":
    main()