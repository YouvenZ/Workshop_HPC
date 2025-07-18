#!/usr/bin/env python3
import time
import argparse
import multiprocessing
import numpy as np
from datetime import datetime

def cpu_intensive_task(n, task_id):
    """CPU-intensive task with task-specific computation"""
    base_computation = sum(i**2 for i in range(n))
    task_specific = task_id * 100000
    return base_computation + task_specific

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task_id', type=int, required=True)
    args = parser.parse_args()
    
    print(f"=== CPU Array Job Demo (Task {args.task_id}) ===")
    print(f"Start time: {datetime.now()}")
    print(f"Available CPUs: {multiprocessing.cpu_count()}")
    print(f"Task ID: {args.task_id}")
    
    # Task-specific computation
    print(f"Running task-specific computation for task {args.task_id}...")
    start = time.time()
    result = cpu_intensive_task(500000, args.task_id)
    end = time.time()
    
    print(f"Task {args.task_id} result: {result}")
    print(f"Computation time: {end - start:.2f} seconds")
    print(f"End time: {datetime.now()}")
    print(f"=== CPU Array Task {args.task_id} Complete ===")

if __name__ == "__main__":
    main()