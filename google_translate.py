from google.cloud import translate_v2 as translate


class Translator():

    def __init__(self):
        self.translate_client = translate.Client()

    def translate(self, text, target):
        result = self.translate_client.translate(text, target_language=target)
        self.input = result["input"]
        self.input_lang = result["detectedSourceLanguage"]
        self.translated = result["translatedText"]
        return self.translated


if __name__ == '__main__':

    text = 'Hello world'
    lang = 'ko'

    tr = Translator()
    translated = tr.translate(text, lang)
    print(translated)
