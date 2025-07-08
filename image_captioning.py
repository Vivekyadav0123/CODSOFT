from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from google.colab import files
from IPython.display import display

# Upload image
uploaded = files.upload()

# Get uploaded file name
image_path = next(iter(uploaded))

# Open the image
image = Image.open(image_path)

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Generate caption
inputs = processor(images=image, return_tensors="pt")
output = model.generate(**inputs)
caption = processor.decode(output[0], skip_special_tokens=True)

# Show result
print("Generated Caption:", caption)
display(image)