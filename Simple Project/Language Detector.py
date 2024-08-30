# pip install langdetect

from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

text = input("Enter your text to detect: ")
detectedLanguage = detect(text)
print(F"The detected language is : {detectedLanguage}")