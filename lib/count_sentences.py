#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        '''Validates if the value is a string'''
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

# method returns true if the value ends in a period and false if it does not.
    def is_sentence(self):
        return self._value.endswith('.')

# method returns true if the value ends with a question mark and false if it does not.    
    def is_question(self):
        return self._value.endswith('?')
    
# method returns true if the value ends with an exclamation mark and false if it does not.  
    def is_exclamation(self):
        return self._value.endswith('!')
    
# method retuns the number of sentences in the value.
    def count_sentences(self):
        value = self.value
        punctuations = ["!", "?"]

        for punc in punctuations:
            value = value.replace(punc, ".")

        sentences = [s for s in value.split('.') if s]

        return len(sentences)



string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())
    