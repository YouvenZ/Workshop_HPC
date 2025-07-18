#!/bin/bash
#SBATCH -p Serveurs-CPU
#SBATCH -J cpu_single_test
#SBATCH -c 4
#SBATCH --mem 8000
#SBATCH --error log/cpu_single_test%j.txt
#SBATCH --output log/cpu_single_test%j.out

srun singularity run --bind /data_GPU/:/data_GPU /data_GPU/rzeghlache/containers/carbure_image.sif python /data_GPU/rzeghlache/test_scripts/cpu_single_demo.py