import torch

if not torch.cuda.is_available():
    raise RuntimeError("CUDA GPU is not available")

device = torch.device("cuda")

a = torch.tensor([1.0, 2.0, 3.0], device=device)
b = torch.tensor([4.0, 5.0, 6.0], device=device)

result = a + b

print("A:", a)
print("B:", b)
print("Result:", result)
print("Result stored on:", result.device)