# Daily Planner

Multi-agent system

## Installation

1. Install uv to manage packages
   
2. Make venv: `uv venv`

3. Install deps: `CUDACXX="/usr/local/cuda/bin/nvcc" CMAKE_ARGS="-DGGML_CUDA=on" uv sync --no-cache -v`
