import numpy as np
from PIL import Image
import random
import string

def random_string(length=83):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_random_image(width, height):
    
    array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    img = Image.fromarray(array)
    
    filename = f"{random_string()}.png"
    #SAVE THIS IMAGE YES IM GONNA WRITE IT OUT ON CAPS BECUSE WHY NOT IM BORED
    img.save(filename)
    print(f"{filename}")

 
generate_random_image(1080, 1920)
generate_random_image(1920, 1080)
generate_random_image(720, 1280)
generate_random_image(1280, 720)
generate_random_image(1440, 2560)
generate_random_image(2560, 1440)