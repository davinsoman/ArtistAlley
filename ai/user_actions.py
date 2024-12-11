import tkinter as tk
from tkinter import filedialog
from ai.model_access import predict_image
import matplotlib.pyplot as plt
from PIL import Image

def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    img_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    return img_path

def display_image(img_path):
    with Image.open(img_path) as img:
        plt.axis("off")
        plt.imshow(img)
        plt.show()

# Example usage
if __name__ == '__main__':
    # Example predictions
    img_path = "/kaggle/input/human-ai-artwork/data/AI_LD_baroque/1-100202515-209882.jpg"
    display_image(img_path)
    prediction = predict_image(img_path)
    print(f"Class prediction: {prediction}")

    img_path = "/kaggle/input/human-ai-artwork/data/Human_Baroque/adriaen-brouwer_drinkers-in-the-yard.jpg"
    display_image(img_path)
    prediction = predict_image(img_path)
    print(f"Class prediction: {prediction}")

    # Allow user to select an image
    img_path = select_image()
    if img_path:
        display_image(img_path)
        prediction = predict_image(img_path)
        print(f"Class prediction: {prediction}")
    else:
        print("No image selected.")