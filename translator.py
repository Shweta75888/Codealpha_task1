from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text
def main():
    print("Language Translator")
    print("===================")
    
    source_text = input("Enter the text to translate: ")
    source_lang = input("Enter the source language (e.g., en for english): ")
    target_lang = input("Enter the target language (e.g., fr for French): ")
    
    translated_text = translate_text(source_text, source_lang, target_lang)
    
    print("\nTranslation:")
    print(translated_text)

if __name__ == "__main__":
    main()

