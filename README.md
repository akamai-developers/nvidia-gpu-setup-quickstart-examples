# nvidia-gpu-setup-quickstart-examples
Sample code for the NVIDIA GPU setup and CUDA video tutorial.


This repository accompanies the video tutorial on setting up an NVIDIA GPU for CUDA and AI workloads on Ubuntu. It contains simple examples that demonstrate how to:

- Verify that the NVIDIA GPU is accessible with PyTorch
- Run basic computations on the GPU
- Run LLM inference using vLLM
- Compile and run CUDA code from source using the CUDA Toolkit

The examples are designed to show the progression from verifying GPU access to running real GPU-accelerated applications.


# Directory structure 
```
nvidia-gpu-setup-quickstart-examples/
│
├── README.md
├── requirements.txt
│
├── 01_check_gpu.py
├── 02_gpu_computation.py
├── 03_vllm_inference.py
│
└── 04_cuda_from_source/
    └── vector_add.cu
```