# Daily Planner

Multi-agent system with llama.cpp (C++/Python) backend

## Installation

1. Install uv to manage packages

2. Make venv: `uv venv`

3. Install deps
  a. If you have llama.cpp installed you don't need llama-cpp-python. You would need to start up your llama-server and pass the http port to a `LlamaCppServerProvider` instance
  b. If you don't have llama.cpp installed, you would want to compile llama-cpp-python with CUDA support by passing the CMAKE flags: `CUDACXX="/usr/local/cuda/bin/nvcc" CMAKE_ARGS="-DGGML_CUDA=on" uv sync --no-cache -v`.<br />
     Naturally you would be using a LlamaCppPythonProvider
