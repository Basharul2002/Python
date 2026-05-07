import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Try enabling drag & drop
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_AVAILABLE = True
except:
    DND_AVAILABLE = False

FORMAT_MAP = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "webp": "WEBP",
    "bmp": "BMP",
    "tiff": "TIFF"
}

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")
        self.root.geometry("500x400")

        self.files = []

        # UI Elements
        self.label = tk.Label(root, text="Drag & Drop Images or Select Files", font=("Arial", 12))
        self.label.pack(pady=20)

        self.drop_area = tk.Label(root, text="Drop Here", bg="#dddddd", width=40, height=10)
        self.drop_area.pack(pady=10)

        if DND_AVAILABLE:
            self.drop_area.drop_target_register(DND_FILES)
            self.drop_area.dnd_bind('<<Drop>>', self.drop_files)

        self.select_btn = tk.Button(root, text="Select Images", command=self.select_files)
        self.select_btn.pack(pady=5)

        self.format_label = tk.Label(root, text="Output Format:")
        self.format_label.pack()

        self.format_entry = tk.Entry(root)
        self.format_entry.pack(pady=5)

        self.convert_btn = tk.Button(root, text="Convert", command=self.convert_images)
        self.convert_btn.pack(pady=20)

    def drop_files(self, event):
        files = self.root.tk.splitlist(event.data)
        self.files.extend(files)
        self.label.config(text=f"{len(self.files)} file(s) loaded")

    def select_files(self):
        files = filedialog.askopenfilenames()
        self.files.extend(files)
        self.label.config(text=f"{len(self.files)} file(s) selected")

    def convert_images(self):
        if not self.files:
            messagebox.showerror("Error", "No files selected!")
            return

        output_format = self.format_entry.get().lower()
        if output_format not in FORMAT_MAP:
            messagebox.showerror("Error", "Unsupported format!")
            return

        output_folder = "converted"
        os.makedirs(output_folder, exist_ok=True)

        success = 0

        for file in self.files:
            try:
                with Image.open(file) as img:
                    if output_format in ["jpg", "jpeg"]:
                        img = img.convert("RGB")

                    base = os.path.splitext(os.path.basename(file))[0]
                    output_path = os.path.join(output_folder, f"{base}.{output_format}")

                    img.save(output_path, FORMAT_MAP[output_format])
                    success += 1
            except Exception as e:
                print(f"Error: {file} -> {e}")

        messagebox.showinfo("Done", f"Converted {success} images!\nSaved in '{output_folder}' folder.")
        self.files = []
        self.label.config(text="Drag & Drop Images or Select Files")


# Run App
if __name__ == "__main__":
    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()

    app = ImageConverterApp(root)
    root.mainloop()
