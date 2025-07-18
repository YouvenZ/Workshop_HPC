#!/bin/bash
#SBATCH -p Serveurs-CPU
#SBATCH -J cpu_array_test
#SBATCH -c 4
#SBATCH --mem 8000
#SBATCH --error log/cpu_array_test%A_%a.txt
#SBATCH --output log/cpu_array_test%A_%a.out
#SBATCH --array=[0-4]%2

srun singularity run --bind /data_GPU/:/data_GPU /data_GPU/rzeghlache/containers/carbure_image.sif python /data_GPU/rzeghlache/test_scripts/cpu_array_demo.py --task_id $SLURM_ARRAY_TASK_ID