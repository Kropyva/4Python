from googletrans import Translator, LANGUAGES
from googletrans.models import Detected

def MyTranslate(text: str, lang: str) -> str:
    try:
        return Translator().translate(text, lang.lower(), 'auto').text
    except:
        return None

def MyLangDetect(text: str) -> Detected:
    try:
        return Translator().detect(text)
    except:
        None

def MyCodeLang(lang: str) -> str:
    lang = lang.lower()
    return LANGUAGES.get(lang, LANGUAGES.get(lang.title(), None))

text = "¿hola, cómo estás?"
lang = "cs"

print(text)
print(MyLangDetect(text))
print(MyTranslate(text, lang))
print(MyCodeLang(lang))
