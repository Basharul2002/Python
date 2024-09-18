#pip install emoji

import emoji

def text_to_emoji(text):

    return emoji.emojize(text)


input_text = input("Enter text with emoji aliases : ")
converted_text = text_to_emoji(input_text)
print("Converted Text with Emojis:", converted_text)
