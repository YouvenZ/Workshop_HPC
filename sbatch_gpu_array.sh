#!/bin/bash
#SBATCH -p GPU48Go
#SBATCH --gres=gpu:1
#SBATCH -c 4
#SBATCH --mem 8000
#SBATCH -J gpu_array_test
#SBATCH --error log/gpu_array_test%A_%a.txt
#SBATCH --output log/gpu_array_test%A_%a.out
#SBATCH --array=[0-4]%2

srun singularity run --nv --bind /data_GPU/:/data_GPU /data_GPU/rzeghlache/containers/carbure_image.sif python /data_GPU/rzeghlache/test_scripts/gpu_array_demo.py --task_id $SLURM_ARRAY_TASK_ID