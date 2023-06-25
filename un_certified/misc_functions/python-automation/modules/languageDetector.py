from textblob import TextBlob

inputSTR = input('\nEnter the string : ')

textblob_obj = TextBlob(inputSTR)

detected_language = textblob_obj.detect_language()

print("\nDetected language : ", detected_language)