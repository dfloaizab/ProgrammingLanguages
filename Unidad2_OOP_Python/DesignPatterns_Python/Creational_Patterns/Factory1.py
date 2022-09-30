
class TranslateEnglish():
    def __init__(self):
        self.translations  = {"mamá":"mom", "papá":"dad"}
    def translate(self, msg):
        return self.translations.get(msg)

class TranslateFrench():
     def __init__(self):
        self.translations  = {"mamá":"mére", "papá":"pére"}
     def translate(self, msg):
        return self.translations.get(msg)

class TranslateGerman():
    def __init__(self):
        self.translations  = {"mamá":"mama", "papá":"papa"}
    def translate(self, msg):
        return self.translations.get(msg)

class TranslationFactory():
    def __init__(self):
        self.translators = { "English":TranslateEnglish, "French": TranslateFrench, "German":TranslateGerman  }
    def return_translator(self, language):
        return self.translators[language]

if __name__ == "__main__":

    my_factory = TranslationFactory()
    my_en_translator = my_factory.return_translator("English")
    my_fr_translator = my_factory.return_translator("French")
    my_gr_translator = my_factory.return_translator("German")
