import numpy as np
from PIL import Image
import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Image Generator")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')

        # Style configuration
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 10), padding=5)
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TCombobox', font=('Arial', 10), padding=5)

        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Size selection
        ttk.Label(main_frame, text="Select Image Size:").pack(pady=5)
        
        self.sizes = {
            "1080x1920 (Portrait FHD)": (1080, 1920),
            "1920x1080 (Landscape FHD)": (1920, 1080),
            "720x1280 (Portrait HD)": (720, 1280),
            "1280x720 (Landscape HD)": (1280, 720),
            "1440x2560 (Portrait 2K)": (1440, 2560),
            "2560x1440 (Landscape 2K)": (2560, 1440)
        }
        
        self.size_var = tk.StringVar()
        size_combo = ttk.Combobox(main_frame, textvariable=self.size_var, values=list(self.sizes.keys()))
        size_combo.pack(pady=5)
        size_combo.set(list(self.sizes.keys())[0])

        # Number of images
        ttk.Label(main_frame, text="Number of Images:").pack(pady=5)
        self.num_images = ttk.Entry(main_frame, width=10)
        self.num_images.pack(pady=5)
        self.num_images.insert(0, "1")

        # Output folder
        if not os.path.exists("The unstopple sf-90 of the won won won"):
            os.makedirs("The unstopple sf-90 of the won won won")

        # Generate button
        generate_btn = ttk.Button(main_frame, text="Generate Images", command=self.generate_images)
        generate_btn.pack(pady=20)

        # Status text
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to generate images...")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, wraplength=350)
        status_label.pack(pady=10)

    def random_string(self, length=10):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_random_image(self, width, height):
        array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        img = Image.fromarray(array)
        filename = f"The unstopple sf-90 of the won won won/random_{self.random_string()}.png"
        img.save(filename)
        return filename

    def generate_images(self):
        try:
            num = int(self.num_images.get())
            if num <= 0:
                raise ValueError("Number of images must be positive")
            if num > 50:
                if not messagebox.askyesno("Warning", "Generating many images might take some time. Continue?"):
                    return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of images")
            return

        selected_size = self.size_var.get()
        if selected_size not in self.sizes:
            messagebox.showerror("Error", "Please select an image size")
            return

        width, height = self.sizes[selected_size]
        
        self.status_var.set("Generating images...")
        self.root.update()
        
        generated_files = []
        for i in range(num):
            filename = self.generate_random_image(width, height)
            generated_files.append(os.path.basename(filename))
            self.status_var.set(f"Generated {i+1}/{num} images...")
            self.root.update()

        self.status_var.set(f"Successfully generated {num} images in The unstopple sf-90 of the won won won folder")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()