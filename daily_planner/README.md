# Daily Planner

Multi-agent system with llama.cpp (C++/Python) backend

## Installation

1. Install uv to manage packages

2. Make venv: `uv venv`

3. Install deps
   1. If you have llama.cpp installed you don't need llama-cpp-python. `uv sync` would suffice. <br/>
      llama-server needs to be run on the side the http port passed to a `LlamaCppServerProvider` instance here.
   2. If you don't have llama.cpp installed, you would want to compile llama-cpp-python with CUDA support by passing the CMAKE flags: `CUDACXX="/usr/local/cuda/bin/nvcc" CMAKE_ARGS="-DGGML_CUDA=on" uv sync --no-cache -v`.<br />
     Naturally you would be using a `LlamaCppPythonProvider` instance here.
