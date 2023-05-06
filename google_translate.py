from google.cloud import translate_v2 as translate


class Translator():

    def __init__(self, target='en'):
        self.translate_client = translate.Client()
        self.default_target = target

    def translate(self, text, target=None):
        if target is None:
            target = self.default_target
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
