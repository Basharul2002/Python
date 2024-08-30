# pip install pip install rembg 


from rembg import remove
from PIL import Image 

inputPath = input("Enter the input path: ")
outputPath = "output.png"

input = Image.open(inputPath)
output = remove(input)

output.save(outputPath)

