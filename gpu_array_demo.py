#!/usr/bin/env python3
import time
import os
import argparse
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

def gpu_computation(task_id):
    """Task-specific GPU computation"""
    try:
        import torch
        if torch.cuda.is_available():
            device = torch.device('cuda')
            size = 500 + task_id * 100
            a = torch.randn(size, size, device=device)
            b = torch.randn(size, size, device=device)
            result = torch.mm(a, b)
            return result.sum().item(), size
        return None, None
    except ImportError:
        return None, None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task_id', type=int, required=True)
    args = parser.parse_args()
    
    print(f"=== GPU Array Job Demo (Task {args.task_id}) ===")
    print(f"Start time: {datetime.now()}")
    print(f"Task ID: {args.task_id}")
    print(f"CUDA_VISIBLE_DEVICES: {os.environ.get('CUDA_VISIBLE_DEVICES', 'Not set')}")
    
    gpu_available, gpu_name, gpu_count = check_gpu()
    print(f"GPU Available: {gpu_available}")
    if gpu_available:
        print(f"GPU Name: {gpu_name}")
        print(f"GPU Count: {gpu_count}")
        
        print(f"Running GPU computation for task {args.task_id}...")
        start = time.time()
        result, matrix_size = gpu_computation(args.task_id)
        end = time.time()
        
        print(f"Task {args.task_id} - Matrix size: {matrix_size}x{matrix_size}")
        print(f"Task {args.task_id} - GPU result: {result}")
        print(f"Computation time: {end - start:.2f} seconds")
    else:
        print("No GPU available, running CPU fallback...")
        start = time.time()
        result = sum(i**2 for i in range(50000 + args.task_id * 10000))
        end = time.time()
        print(f"Task {args.task_id} - CPU result: {result}")
        print(f"Computation time: {end - start:.2f} seconds")
    
    print(f"End time: {datetime.now()}")
    print(f"=== GPU Array Task {args.task_id} Complete ===")

if __name__ == "__main__":
    main()