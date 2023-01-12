# #Task_2
class TextProcessor:
    def __init__(self):
        self._punctuation = '.,!?:;*'

    def get_clean_string(self, my_text):
        clean_text = ''
        for i in my_text:
            if i not in self._punctuation:
                clean_text += i
        return clean_text

    def is_punctuation(self, char):
        return char in self._punctuation

# t = TextProcessor()
# print(t.get_clean_string('Hello, Python.!!!; Is this my program?;'))
# print(t.is_punctuation(':'))


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, my_text):
        self.__clean_string = self.__text_processor.get_clean_string(my_text)
        return self.__clean_string

    @property
    def clean_string(self):
        print(f'It is a clean text without punctuation {self.__clean_string}')
        return self.__clean_string


# t2 = TextLoader()
# print(t2.set_clean_string('Hello, Python.!!!; Is this my program?;'))
# print(t2.clean_string)


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, my_string):
        cleaned_text = []
        for i in my_string:
            clean_string = self._text_loader.set_clean_string(i)
            cleaned_text.append(clean_string)
        return cleaned_text

# d = DataInterface()
# print(d.process_texts('Hello:;, Python.!!!?'))









