import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
# import ipywidgets as widgets
# from ipywidgets import interact

# %cd ~/../notebooks

## Use the lists below to select our model type, image output resolution, and the computer number format for inference
device = 'cuda'
## We recommend either v1-5 (index 1) or v2 (index 2)
model_id = ['CompVis/stable-diffusion-v1-4',"../datasets/stable-diffusion-diffusers/stable-diffusion-v1-5/",'../datasets/stable-diffusion-diffusers-v2/stable-diffusion-2/']
## We strongly recommend using the v1-5 and v1-4 models with size 512, and the v2 models with size 768.
size = [512, 768]
## If you are using a GPU with ~ 8 GBs of RAM, like the Free-GPU Notebooks, then use torch.float16
## otherwise, either selection works
dtype = [torch.float16, torch.float32]


# Set your values here - defaults are for v2, size 768 x 768 with FP16 computer number format
model_ = model_id[2]
size_ = size[1] 
precision = dtype[0]
