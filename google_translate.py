import sys
from google.cloud import translate_v2 as translate


class Translator():

    def __init__(self, target=None):
        self.translate_client = translate.Client()
        self.default_target = target

    def translate(self, text, target=None):
        if target is None:
            target = self.default_target
        if target is None:
            print("You need to set target language")
            sys.exit(1)
        result = self.translate_client.translate(text, target_language=target)
        self.input = result["input"]
        self.input_lang = result["detectedSourceLanguage"]
        self.translated = result["translatedText"]
        return self.translated


if __name__ == '__main__':

    text = 'Hello world'
    lang = 'ko'

    tr = Translator(lang)
    translated = tr.translate(text)
    print(translated)
