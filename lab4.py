class Dictionary:
    def __init__(self):
        self.words = {}

    def add_word(self, word, *translations):

        self.words[word] = set(translations)

    def remove_word(self, word):

        if word in self.words:
            del self.words[word]
            print(f'Слово "{word}" видалено зі словника.')
        else:
            print(f'Слово "{word}" не знайдено у словнику.')

    def remove_translated(self, word, invalid_translation):

        if word in self.words:
            if invalid_translation in self.words[word]:
                self.words[word].remove(invalid_translation)
                print(f'Переклад "{invalid_translation}" видалено для слова "{word}".')
            else:
                print(f'Переклад "{invalid_translation}" не знайдено для слова "{word}".')
        else:
            print(f'Слово "{word}" не знайдено у словнику.')

    def display_dictionary(self):

        print("Словник:")
        for word, translations in self.words.items():
            print(f'{word}: {", ".join(translations)}')




my_dictionary = Dictionary()


my_dictionary.add_word("apple", "яблуко"
                       )
my_dictionary.add_word("book", "книга", "журнал")


my_dictionary.display_dictionary()


my_dictionary.remove_word("apple")
my_dictionary.display_dictionary()

my_dictionary.remove_translated("book", "журнал")
my_dictionary.display_dictionary()
