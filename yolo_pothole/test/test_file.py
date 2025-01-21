import torch

cuda = torch.cuda.is_available()
print(cuda)

device = torch.device('cuda:0'if cuda else 'cpu')
print(device)

gpu = torch.cuda.get_device_name(0)
print(gpu)