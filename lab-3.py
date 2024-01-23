from googletrans import Translator, LANGUAGES
from googletrans.models import Detected
from tabulate import tabulate
import pandas as pandas

def MyTranslate(text: str, dest: str, src: str = 'auto') -> str:
    try:
        return Translator().translate(text, dest.lower(), src).text
    except:
        return None

def MyLangDetect(text: str, set: str = 'all') -> (str | Detected):
    try:
        translated = Translator().detect(text)

        if set == 'lang':
            return translated.lang
        if set == 'confidence':
            return translated.confidence
        if set == 'all':
            return translated
    except:
        None

def MyCodeLang(lang: str) -> str:
    lang = lang.lower()

    for key, value in LANGUAGES.items():
        if key == lang:
            return value
        if value == lang:
            return key
        
    return None

def MyLanguageList(text: str = '', out: str = 'screen'):
    codes = list(LANGUAGES.keys())
    table = {'N': range(1, len(LANGUAGES) + 1), 'Languages': list(LANGUAGES.values()), 'ISO-639': codes}

    if text:
        table['Text'] = [MyTranslate(text, lang) for lang in codes]

    table = pandas.DataFrame(table)

    if out == 'screen':
        print(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex=False))
        return "The table is on the screen\n"
    if out == 'file':
        with open('pytable.txt', 'w', encoding='utf-8') as file:
            file.write(tabulate(table, headers='keys', tablefmt='fancy_grid', showindex=False))
        return "The table saved into pytable.txt\n"       
    
    return "The argument 'out' is wrong\n"

text = "¿hola, cómo estás?"
lang = "Czech"

print(text)
print(MyLangDetect(text))
print(MyTranslate(text, lang))
print(MyCodeLang(lang))
print(MyLanguageList('hello', 'file'))