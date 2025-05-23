# cli.py
from .core import load_translations, translate

def main():
    translations = load_translations()
    if not translations:
        print("No translations found. Ensure translations.txt exists in package data.")
        return

    sentence = input("Enter sentence to translate: ")
    print("\nTranslated sentence:")
    print(translate(sentence, translations))