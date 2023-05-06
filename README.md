# Google Translate
Python translation software using Google Translate
[API](https://cloud.google.com/translate)

You need to set `GOOGLE_APPLICATION_CREDENTIALS` environment variable.


## Examples

``` python
from google_translate import Translator

text = 'Hello world'
lang = 'ko'

tr = Translator(lang)
translated = tr.translate(text)
```

``` python
from google_translate import Translator

text = 'Hello world'
lang = 'ko'

tr = Translator()
translated = tr.translate(text, lang)
```

## Supported Languages
[List](https://cloud.google.com/translate/docs/languages)

## Dependency
- google-cloud-translate
