 
from deep_translator import GoogleTranslator 
class TranslateClass(object): 
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
    def __repr__(self): 
        translated = GoogleTranslator(source='auto', target=self.lang).translate(self.word)
        return translated

if __name__ == '__main__':
    translate = input('Enter Word/Sentence: ')
    language = input( ' Enter the language (de, fr, it, es, bg): ' )
    # Translate to Deutsch --> insert "de' wint TranslateClass translate
    print(TranslateClass(translate, language))