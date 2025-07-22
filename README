# HPC Workshop Tutorial

A comprehensive tutorial for High Performance Computing workflows using Singularity/Apptainer containers, SLURM job scheduling, and machine learning workloads.

## Workshop Overview

This workshop covers:
- Container creation and management with Singularity/Apptainer
- SLURM job submission (single and array jobs)
- GPU and CPU workload optimization
- Data transfer and bind mounting
- Environment setup with Conda

## Prerequisites

- Basic Linux command line knowledge
- Access to an HPC cluster with SLURM
- Singularity/Apptainer installed
- SSH access to remote cluster

## Directory Structure

```
HPC_workshop/
├── containers/
│   ├── anaconda_recipe.def     # Conda-based container definition
│   ├── python-ml.def          # Basic Python ML container
│   ├── recipe.def             # CUDA-enabled container
│   └── workshop.yml           # Conda environment specification
├── scripts/
│   ├── bind_script.py         # Test bind mount functionality
│   ├── script.py              # Container environment testing
│   ├── cpu_single_demo.py     # Single CPU job demo
│   ├── cpu_array_demo.py      # CPU array job demo
│   ├── gpu_single_demo.py     # Single GPU job demo
│   └── gpu_array_demo.py      # GPU array job demo
├── slurm/
│   ├── sbatch_cpu_single.sh   # SLURM script for single CPU job
│   ├── sbatch_cpu_array.sh    # SLURM script for CPU array jobs
│   ├── sbatch_gpu_single.sh   # SLURM script for single GPU job
│   └── sbatch_gpu_array.sh    # SLURM script for GPU array jobs
├── data_transfer/
│   ├── copy_code.sh           # Transfer code to cluster
│   ├── copy_data.sh           # Transfer data to cluster
│   ├── copy_image.sh          # Transfer container images
│   └── rsync_ignore.text      # Files to exclude from transfer
├── csv/                       # Sample datasets
│   ├── ai4i2020.csv
│   ├── data.csv
│   └── used_car_price_dataset_extended.csv
├── local/                     # Local files (not transferred)
└── log/                       # Job output logs
└── README                    # This file
```

## Quick Start Guide

### 1. Container Creation

#### Basic Python ML Container
```bash
# Build basic Python container
sudo singularity build python-ml.sif containers/python-ml.def
```

#### Conda Environment Container
```bash
# Build conda-based container with full data science stack
sudo singularity build workshop.sif containers/anaconda_recipe.def
```

#### CUDA-enabled Container
```bash
# Build GPU-enabled container
sudo singularity build gpu-ml.sif containers/recipe.def
```

### 2. Testing Containers

#### Test Basic Functionality
```bash
# Test container environment
singularity exec python-ml.sif python scripts/script.py

# Test bind mounting with CSV data
singularity exec --bind ./scripts/csv:/data python-ml.sif python scripts/bind_script.py
```

### 3. Data Transfer to Cluster

#### Transfer Code
```bash
# Edit copy_code.sh with your cluster details
./data_transfer/copy_code.sh
```

#### Transfer Data
```bash
# Edit copy_data.sh with your paths
./data_transfer/copy_data.sh
```

#### Transfer Container Images
```bash
# Edit copy_image.sh with your container path
./data_transfer/copy_image.sh
```

### 4. Job Submission

#### Single CPU Job
```bash
sbatch slurm/sbatch_cpu_single.sh
```

#### CPU Array Job
```bash
sbatch slurm/sbatch_cpu_array.sh
```

#### Single GPU Job
```bash
sbatch slurm/sbatch_gpu_single.sh
```

#### GPU Array Job
```bash
sbatch slurm/sbatch_gpu_array.sh
```

## Container Definitions

### Basic Python ML (

containers/python-ml.def

)
Simple container with essential ML libraries:
- numpy, pandas, scikit-learn, matplotlib

### Conda Environment (

containers/anaconda_recipe.def

)
Full data science environment using conda:
- Jupyter Lab, seaborn, scipy, and more
- Based on 

workshop.yml


- Includes 200+ packages for comprehensive data science workflows

### GPU-enabled (

containers/recipe.def

)
CUDA-enabled container for GPU workloads:
- PyTorch with CUDA support
- NVIDIA runtime base image

## Demo Scripts

### CPU Demos
- 

cpu_single_demo.py

 - Single-threaded CPU intensive task using 

cpu_intensive_task


- 

cpu_array_demo.py

 - Parallel CPU tasks with different parameters

### GPU Demos
- 

gpu_single_demo.py

 - Single GPU computation with 

check_gpu

 and 

gpu_computation


- 

gpu_array_demo.py

 - Multiple GPU tasks with task-specific matrix sizes

### Testing Scripts
- 

script.py

 - Environment and package testing with 

test_python_info

, 

test_environment

, and 

test_package_imports


- 

bind_script.py

 - Bind mount and CSV file testing with 

test_bind_mount

 and 

test_csv_files



## SLURM Configuration

### Resource Allocation Examples

#### CPU Jobs
```bash
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=01:00:00
```

#### GPU Jobs
```bash
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH --time=02:00:00
```

#### Array Jobs
```bash
#SBATCH --array=1-10
#SBATCH --cpus-per-task=2
```

## Data Management

### Bind Mounting
```bash
# Mount data directory
singularity exec --bind /path/to/data:/data container.sif python script.py

# Multiple bind mounts
singularity exec --bind /data:/data,/results:/output container.sif python analysis.py
```

### Sample Datasets
The workshop includes sample datasets in 

csv

:
- 

ai4i2020.csv

 - Industrial AI dataset
- 

used_car_price_dataset_extended.csv

 - Automotive pricing data
- 

data.csv

 - General dataset for testing

## Workflow Examples

### Complete ML Pipeline
```bash
# 1. Build container
sudo singularity build ml-pipeline.sif containers/anaconda_recipe.def

# 2. Transfer to cluster
./data_transfer/copy_code.sh
./data_transfer/copy_image.sh

# 3. Submit job
sbatch slurm/sbatch_gpu_single.sh
```

### Parameter Sweep with Array Jobs
```bash
# Submit array job for hyperparameter tuning
sbatch --array=1-100 slurm/sbatch_cpu_array.sh
```

### Testing Workflow
```bash
# Test container locally
singularity exec --bind ./scripts/csv:/data workshop.sif python scripts/bind_script.py

# Test GPU functionality
singularity exec --nv workshop.sif python scripts/gpu_single_demo.py
```

## Advanced Features

### Conda Workflow
For detailed conda environment management, see 

conda_workflow.md

 which covers:
- Creating conda environments
- Exporting to YAML
- Building Apptainer images
- Adding new packages in sandbox mode

### Data Transfer Optimization
The 

data_transfer

 scripts use rsync with optimized settings:
- Compression for faster transfer
- Progress monitoring
- Exclude patterns from 

rsync_ignore.text


- Error handling and logging

## Troubleshooting

### Common Issues

1. **Container build fails**: Check sudo privileges and disk space
2. **Bind mount not working**: Verify path exists and permissions
3. **GPU not detected**: Ensure NVIDIA drivers and `--nv` flag
4. **SLURM job fails**: Check resource requests and queue limits

### Debugging Commands
```bash
# Check container
singularity inspect container.sif

# Test interactively
singularity shell container.sif

# Check SLURM status
squeue -u $USER
sacct -j <job_id>

# Test GPU availability
singularity exec --nv container.sif python -c "import torch; print(torch.cuda.is_available())"
```

### Log Files
Job outputs are stored in the 

log

 directory:
- CPU jobs: `cpu_single_test<job_id>.out`
- GPU jobs: `gpu_single_test<job_id>.out`
- Array jobs: `cpu_array_test<job_id>_<array_id>.out`

## Documentation References

- Complete Conda Workflow Guide - Detailed conda environment setup
- [SLURM Documentation](https://slurm.schedmd.com/documentation.html)
- [Singularity User Guide](https://sylabs.io/guides/latest/user-guide/)

## Workshop Modules

1. **Container Basics** - Building and testing containers with 

python-ml.def


2. **Data Management** - Bind mounts and file transfers using 

bind_script.py


3. **Job Scheduling** - SLURM single and array jobs in 

slurm


4. **GPU Computing** - CUDA containers and GPU jobs with 

gpu_single_demo.py


5. **Workflow Optimization** - Best practices and troubleshooting

## Environment Details

The  workshop.yml

 includes:
- **Core Libraries**: numpy, pandas, matplotlib, seaborn, scipy, scikit-learn
- **Jupyter Stack**: jupyterlab, jupyter, ipython, ipykernel
- **Development Tools**: python 3.10.18, pip, setuptools
- **Scientific Computing**: mkl, numexpr, threadpoolctl
- **Visualization**: plotly, matplotlib-base, qt libraries


## License

This workshop material is provided for educational purposes. Please check individual dataset licenses in the csv directory.