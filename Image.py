import numpy as np
from PIL import Image
import random
import string

select = input("size? " \
"1. 1080x1920" \
"2. 1920x1080" \
"3. 720x1280" \
"4. 1280x720" \
"5. 1440x2560" \
"6. 2560x1440 " \
)
times = int(input("how many images? "))
#THIS SHOULD GENERATE RANDOM IMAGE NAME TYPA SHT U KNOW
def random_string(length=83):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
# THIS SHT GENERATES RANDOM IMAGE WITH RANDOM THINGS ON IT (Maybe u get the sf-90 motor photo idk )
def generate_random_image(width, height):
    
    array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    img = Image.fromarray(array)
    
    filename = f"{random_string()}.png"
    #SAVE THIS IMAGE YES IM GONNA WRITE IT OUT ON CAPS BECUSE WHY NOT IM BORED
    img.save(filename)
    print(f"{filename}")

for _ in range(times):
    if select == "1":
        generate_random_image(1080, 1920)
    if select == "2":
        generate_random_image(1920, 1080)
    if select == "3":
        generate_random_image(720, 1280)
    if select == "4":
        generate_random_image(1280, 720)
    if select == "5":
        generate_random_image(1440, 2560)
    if select == "6":
        generate_random_image(2560, 1440)