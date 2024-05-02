from textblob import TextBlob

text = input("Enter your text: ")
blob = TextBlob(text)

corrected_blob = blob.correct()

print("Orginal Text: ", blob)
print("Corrected  Text: ", corrected_blob)