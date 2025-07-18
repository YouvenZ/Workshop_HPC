#!/usr/bin/env python3
"""
Container Environment Test Script
Tests imports, versions, and environment information
"""

import sys
import os
from pathlib import Path
import platform

def print_separator(title):
    """Print a formatted separator with title"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def test_python_info():
    """Test Python installation and version"""
    print_separator("PYTHON INFORMATION")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Python path: {sys.path[:3]}...")  # Show first 3 paths
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")

def test_environment():
    """Test environment variables and paths"""
    print_separator("ENVIRONMENT INFORMATION")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Home directory: {Path.home()}")
    print(f"PATH variable length: {len(os.environ.get('PATH', '').split(':'))}")
    print(f"User: {os.environ.get('USER', 'unknown')}")
    
    # Check if we're in a container
    if os.path.exists('/.singularity.d'):
        print("✓ Running inside Singularity container")
    elif os.path.exists('/.dockerenv'):
        print("✓ Running inside Docker container")
    else:
        print("• Running on host system")

def test_package_imports():
    """Test required package imports and versions"""
    print_separator("PACKAGE TESTING")
    
    packages = [
        ('numpy', 'np'),
        ('pandas', 'pd'),
        ('sklearn', None),
        ('matplotlib', 'plt')
    ]
    
    successful_imports = 0
    
    for package_name, alias in packages:
        try:
            if package_name == 'sklearn':
                import sklearn
                module = sklearn
                import_name = 'sklearn'
            elif package_name == 'matplotlib':
                import matplotlib.pyplot as plt
                module = plt.matplotlib
                import_name = 'matplotlib.pyplot'
            else:
                module = __import__(package_name)
                import_name = package_name
            
            version = getattr(module, '__version__', 'version not available')
            print(f"✓ {import_name}: {version}")
            successful_imports += 1
            
        except ImportError as e:
            print(f"✗ {package_name}: FAILED - {e}")
        except Exception as e:
            print(f"? {package_name}: ERROR - {e}")
    
    return successful_imports

def test_basic_functionality():
    """Test basic functionality of imported packages"""
    print_separator("FUNCTIONALITY TESTING")
    
    try:
        import numpy as np
        # Test numpy
        arr = np.array([1, 2, 3, 4, 5])
        result = np.mean(arr)
        print(f"✓ NumPy calculation: mean([1,2,3,4,5]) = {result}")
        
        import pandas as pd
        # Test pandas
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print(f"✓ Pandas DataFrame created: shape {df.shape}")
        
        from sklearn.datasets import make_classification
        # Test sklearn
        X, y = make_classification(n_samples=100, n_features=4, random_state=42)
        print(f"✓ Sklearn dataset created: {X.shape[0]} samples, {X.shape[1]} features")
        
        import matplotlib
        # Test matplotlib (backend check)
        backend = matplotlib.get_backend()
        print(f"✓ Matplotlib backend: {backend}")
        
        return True
        
    except Exception as e:
        print(f"✗ Functionality test failed: {e}")
        return False

def test_file_operations():
    """Test file I/O operations"""
    print_separator("FILE OPERATIONS TESTING")
    
    try:
        # Test write permissions
        test_file = "container_test.txt"
        with open(test_file, 'w') as f:
            f.write("Container test successful!\n")
        
        # Test read permissions
        with open(test_file, 'r') as f:
            content = f.read().strip()
        
        # Cleanup
        os.remove(test_file)
        
        print(f"✓ File I/O test: '{content}'")
        return True
        
    except Exception as e:
        print(f"✗ File I/O test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🐍 CONTAINER ENVIRONMENT TEST")
    print(f"Script executed from: {__file__}")
    
    # Run all tests
    test_python_info()
    test_environment()
    successful_imports = test_package_imports()
    functionality_ok = test_basic_functionality()
    file_ops_ok = test_file_operations()
    
    # Summary
    print_separator("SUMMARY")
    print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"Successful imports: {successful_imports}/4")
    print(f"Functionality test: {'✓ PASSED' if functionality_ok else '✗ FAILED'}")
    print(f"File operations: {'✓ PASSED' if file_ops_ok else '✗ FAILED'}")
    
    # Overall status
    all_tests_passed = (successful_imports == 4 and functionality_ok and file_ops_ok)
    status = "🎉 ALL TESTS PASSED" if all_tests_passed else "⚠️  SOME TESTS FAILED"
    print(f"\nContainer status: {status}")
    
    return 0 if all_tests_passed else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)