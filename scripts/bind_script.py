#!/usr/bin/env python3
"""
Simple Bind Mount Test Script
Tests if bind mount is working by reading CSV files
"""

import sys
import os
from pathlib import Path
import pandas as pd

def print_separator(title):
    """Print a formatted separator with title"""
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")

def test_bind_mount():
    """Test if bind mount is working correctly"""
    print_separator("BIND MOUNT TEST")
    
    # Expected bind mount path
    bind_path = Path('/data')
    
    # Check if bind mount directory exists
    if not bind_path.exists():
        print(f"❌ ERROR: Bind mount directory not found: {bind_path}")
        print("   Make sure to run with: --bind /home/youven/code/HPC_workshop/csv:/data")
        return False
    
    print(f"✅ Bind mount directory found: {bind_path}")
    
    # List contents of bind mount
    try:
        contents = list(bind_path.iterdir())
        print(f"📁 Contents of {bind_path}:")
        for item in contents:
            print(f"   - {item.name}")
    except Exception as e:
        print(f"❌ ERROR: Cannot list directory contents: {e}")
        return False
    
    return True

def test_csv_files():
    """Test reading CSV files from bind mount"""
    print_separator("CSV FILES TEST")
    
    # Expected CSV files
    expected_files = [
        'ai4i2020.csv',
        'data.csv', 
        'used_car_price_dataset_extended.csv'
    ]
    
    bind_path = Path('/data')
    results = []
    
    for filename in expected_files:
        file_path = bind_path / filename
        
        print(f"\n🔍 Testing: {filename}")
        
        # Check if file exists
        if not file_path.exists():
            print(f"   ❌ File not found: {file_path}")
            results.append(False)
            continue
        
        print(f"   ✅ File found: {file_path}")
        
        # Try to read the CSV
        try:
            df = pd.read_csv(file_path)
            print(f"   📊 Shape: {df.shape}")
            print(f"   📋 Columns: {list(df.columns)[:5]}{'...' if len(df.columns) > 5 else ''}")
            
            # Show first few rows info
            print(f"   📈 Memory usage: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
            
            results.append(True)
            
        except Exception as e:
            print(f"   ❌ ERROR reading CSV: {e}")
            results.append(False)
    
    return all(results)

def main():
    """Main function"""
    print("🔗 BIND MOUNT CSV TEST")
    print(f"Script location: {__file__}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Test bind mount
    bind_working = test_bind_mount()
    
    if not bind_working:
        print("\n❌ BIND MOUNT FAILED")
        print("\nTo fix this, run the container with:")
        print("singularity exec --bind /home/youven/code/HPC_workshop/csv:/data python-ml.sif python test_bind.py")
        return 1
    
    # Test CSV files
    csv_working = test_csv_files()
    
    # Summary
    print_separator("SUMMARY")
    if bind_working and csv_working:
        print("🎉 ALL TESTS PASSED!")
        print("✅ Bind mount is working correctly")
        print("✅ All CSV files are readable")
        return 0
    else:
        print("⚠️  SOME TESTS FAILED")
        print(f"   Bind mount: {'✅' if bind_working else '❌'}")
        print(f"   CSV files: {'✅' if csv_working else '❌'}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)