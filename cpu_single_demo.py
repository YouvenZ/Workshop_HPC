#!/usr/bin/env python3
import time
import multiprocessing
import numpy as np
from datetime import datetime

def cpu_intensive_task(n):
    """Simple CPU-intensive task"""
    return sum(i**2 for i in range(n))

def main():
    print(f"=== CPU Single Job Demo ===")
    print(f"Start time: {datetime.now()}")
    print(f"Available CPUs: {multiprocessing.cpu_count()}")
    
    # CPU-intensive computation
    print("Running CPU-intensive task...")
    start = time.time()
    result = cpu_intensive_task(1000000)
    end = time.time()
    
    print(f"Result: {result}")
    print(f"Computation time: {end - start:.2f} seconds")
    print(f"End time: {datetime.now()}")
    print("=== CPU Single Job Complete ===")

if __name__ == "__main__":
    main()