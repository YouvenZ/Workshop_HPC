#!/bin/bash
#SBATCH -p GPU24Go,GPU11Go
#SBATCH --gres=gpu:1
#SBATCH -c 4
#SBATCH --mem 8000
#SBATCH -J gpu_single_test
#SBATCH --error log/gpu_single_test%j.txt
#SBATCH --output log/gpu_single_test%j.out

srun singularity run --nv --bind /data_GPU/:/data_GPU /data_GPU/rzeghlache/containers/carbure_image.sif python /data_GPU/rzeghlache/test_scripts/gpu_single_demo.py