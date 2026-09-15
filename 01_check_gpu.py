import torch

print("PyTorch version:", torch.__version__)
print("CUDA runtime version:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))