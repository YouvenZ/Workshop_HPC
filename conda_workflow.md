# Complete Guide: Conda Environment to Apptainer Image

## Step 1: Create Conda Environment

### Create New Data Science Environment
```bash
# Create environment with specific Python version
conda create -n data_env python=3.9

# Activate environment
conda activate data_env

# Install core data science packages
conda install numpy pandas matplotlib seaborn scipy scikit-learn
conda install jupyter jupyterlab plotly statsmodels xarray dask

# Install additional packages from conda-forge
conda install -c conda-forge openpyxl

# Install pip packages if needed
```

## Step 2: Export Environment to YAML

```bash
# Make sure your environment is activated
conda activate data_env

# Export current environment (recommended)
conda env export --no-builds > data_env.yml

# Verify the YAML file
cat data_env.yml

## Step 3: Create Apptainer Definition File

Create 

anaconda_recipe.def

:

```plaintext
Bootstrap: docker
From: continuumio/miniconda3

%files
    data_env.yml /opt/

%post
    # Define environment name
    ENV_NAME="data_env"
    CONFIG_FILE="/opt/data_env.yml"
    
    # Create conda environment with specific name
    /opt/conda/bin/conda env create -f ${CONFIG_FILE} -n ${ENV_NAME}
    
    # Clean up conda cache to reduce image size
    /opt/conda/bin/conda clean -afy

%environment
    export ENV_NAME="data_env"
    export PATH="/opt/conda/envs/${ENV_NAME}/bin:$PATH"

%runscript
    exec /opt/conda/envs/${ENV_NAME}/bin/"$@"
```

## Step 4: Build Apptainer Image

```bash
# Build the image
apptainer build data_env.sif anaconda_recipe.def

# If you need fakeroot privileges
apptainer build --fakeroot data_env.sif anaconda_recipe.def

# Build with verbose output for debugging
apptainer build --verbose data_env.sif anaconda_recipe.def

# Build in sandbox mode for testing (optional)
apptainer build --sandbox data_env_sandbox/ anaconda_recipe.def
```








## Step 5: Test the Image

```bash
# Verify build was successful
apptainer inspect data_env.sif

# Check conda environments
apptainer exec data_env.sif conda info --envs

# Test Python and core packages
apptainer exec data_env.sif python --version
apptainer exec data_env.sif python -c "import numpy, pandas, matplotlib; print('All packages imported successfully')"

# Test specific data science libraries
apptainer exec data_env.sif python -c "import sklearn, scipy, seaborn; print('Data science libraries working')"

# Interactive shell
apptainer shell data_env.sif
```

## Step 6: Use the Image

### Running Python Scripts
```bash
# Run Python scripts
apptainer exec data_env.sif python analysis.py

# Run with mounted data directory
apptainer exec --bind /path/to/data:/data data_env.sif python analysis.py
```



## Step 7 bis: Add new pip package

# Build in sandbox mode for installing new packages


```bash
#create a sandbox (local directory associated to full image)

apptainer build --sandbox data_env_sandbox/ data_env.sif 

#run shell inside the sandbox

apptainer shell --writable data_env_sandbox/ 

# The little trick to activate anaconda env

. /opt/conda/etc/profile.d/conda.sh

## Activation of our env


conda activate data_env

## Installation of some libraries

pip install xgboost


## Recreate a singularity from the image 

apptainer build data_env_new.sif  data_env_sandbox/

## Test the image before and after


apptainer run data_env.sif python -c "import xgboost,sklearn, scipy, seaborn; print('Data science libraries working')"


apptainer run data_env_new.sif python -c "import xgboost, sklearn, scipy, seaborn; print('Data science libraries working')"



```



### Interactive Sessions
```bash
# Interactive Python session
apptainer exec data_env.sif python

# Interactive shell with environment
apptainer shell data_env.sif

# Run as application
apptainer run data_env.sif python main_analysis.py
```

## Step 8: File Structure

Your project directory should look like:
```
project/
├── data_env.yml
├── anaconda_recipe.def
├── analysis.py
├── main_analysis.py
└── data_env.sif (after build)
```

## Example Complete Workflow

```bash
# 1. Create environment
conda create -n data_env python=3.9
conda activate data_env
conda install numpy pandas matplotlib seaborn scipy scikit-learn jupyter

# 2. Export to YAML
conda env export --no-builds > data_env.yml

# 3. Create definition file (as shown above)

# 4. Build image
apptainer build data_env.sif anaconda_recipe.def

# 5. Test
apptainer exec data_env.sif python -c "import pandas; print('Success!')"

# 6. Use
apptainer exec data_env.sif python my_analysis.py
```
