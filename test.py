from googletrans import Translator

translator = Translator()

def translate_text(text, to_language):
    translation = translator.translate(text, dest=to_language)
    return translation.text


text_block = 'Mulțumim pentru interesul aratat siteului nostru. Acesta este un work-in-progress si pot aparea multe probleme in rephrasing. Asteptam cu nerabdare feedback-ul dumneavoastra !'
slight_text = translate_text(translate_text(text_block, 'en'), 'ro')
print(slight_text)
