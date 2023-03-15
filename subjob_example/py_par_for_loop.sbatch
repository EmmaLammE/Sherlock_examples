#!/bin/bash
#SBATCH --job-name=py_add
#SBATCH --time=00:05:00
#SBATCH --mem=1GB
#SBATCH -p serc
#SBATCH -c 1
#SBATCH -o out_%j.out
#SBATCH -e err_%j.err

# below you run/call your code, load modules, python, Matlab, R, etc.
# and do any other scripting you want
# lines that begin with #SBATCH are directives (requests) to the scheduler-SLURM module load python/3.6.1
python3 large_add.py 