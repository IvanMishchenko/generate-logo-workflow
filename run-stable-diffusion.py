import torch
from diffusers import StableDiffusionPipeline
from gradient import ModelsClient
from gradient import NotebooksClient
from gradient import MachinesClient

# model_id = "CompVis/stable-diffusion-v1-4"
# device = "cuda"

notebook = NotebooksClient('8acb785a15e4232e4c3ba395fcfd8d')
machine = MachinesClient('8acb785a15e4232e4c3ba395fcfd8d')
print('machine---->>', machine.list())
print('notebook---->>', notebook.list())

# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# pipe = pipe.to(device)

# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]  
    
# image.save("astronaut_rides_horse.png")
