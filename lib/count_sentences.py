# #!/usr/bin/env python3


# MyString
# Create the MyString class and give it a value property. The class should verify that the value is a string before assigning it. The default value of value should be the empty string, ''.

# is_sentence()
# Define an instance method is_sentence() that returns True if the value ends in a period and False if it does not.

# Hint: You might want to take a look at the list of built in string methods above to see if there's something there that can help you.

# is_question()
# This method should return True if the value ends with a question mark and False if it does not.

# is_exclamation()
# This method should return True if the value ends with an exclamation mark and False if it does not.

# count_sentences()
# What we'd like to be able to do is call a count_sentences() method on a MyString instance, and get back a, well, count of sentences in its value. In other words:

# string = MyString()
# string.value = "This is a string! It has three sentences. Right?"
# string.count_sentences()
# # => 3
# This is a tricky task in any language, but Python provides us a few tools to streamline the process:

# str.replace(old, new)Links to an external site. will replace any instances of old in str with new.
# str.split(pattern)Links to an external site. will split a string into a list using the provided pattern as the separator.
# The reLinks to an external site. module (covered later on in this phase's optional Regular Expressions module) will allow you to search for multiple patterns at once. If you're feeling bold, check out the linked documentation and give it a shot!
# Remember to consider edge cases, such as the following sentence:

# This, well, is a sentence. This is too!! And so is this, I think? Woo...
# What would happen if we split this sentence on the punctuation characters? We would end up with a list that contains empty strings as well as strings containing sentences. How would you eliminate empty strings from a list?

import re

class MyString:
    
    def __init__(self, value=''):
        self._value = ''
        self.value = value  

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self.value.strip().endswith('.')
    
    def is_question(self):
        return self.value.strip().endswith('?')
    
    def is_exclamation(self):
        return self.value.strip().endswith('!')
    
    def count_sentences(self):
        # Split the value into a list of sentences using the regex pattern '[.!?]+'

        sentences = re.split(r'[.!?]+', self.value)
        
        # Remove empty strings from the list and return the count of non-empty strings.
        return len([s for s in sentences if s.strip()])




# Test cases:

    # Testing the MyString class and its methods.
if __name__ == "__main__":
    string = MyString()
    
    string.value = "This is a string. It has three sentences."
    assert string.is_sentence() == True

    string.value = "Is this a question?   "
    assert string.is_question() == True  

    string.value = "Wow!"
    assert string.is_exclamation() == True  

    string.value = "Wow! Really? "
    assert string.is_exclamation() == False  

    string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
    assert string.count_sentences() == 4  

    print("All done and passed!")
