# core.py
import importlib.resources

def load_translations():
    """Load translations from package data"""
    translations = {}
    try:
        with importlib.resources.open_text('translator.data', 'translations.txt') as file:
            for line in file:
                line = line.strip()
                if ':' in line:
                    key, value = line.split(':', 1)
                    translations[key] = value
    except FileNotFoundError:
        pass  # Handled in parent function
    return translations

def translate(sentence, translations):
    """Core translation logic"""
    return ' '.join([translations.get(word, word) for word in sentence.split()])