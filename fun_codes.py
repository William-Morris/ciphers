#
#William Morris
#ciphers.py
"""
A collection of simple ecryption methods gathered from doing practice exercises
in python. These types of things keep popping up. 
"""
import string

def caeser_cipher(secret_phrase, shift_value):
    """
    The key idea behind the Caesar cipher is to replace each letter by a letter
    some fixed number of positions down the alphabet. For example, if we want
    to create a cipher shifting by 3, you will get the following mapping:
    Plain: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Cipher: DEFGHIJKLMNOPQRSTUVWXYZABC
    source:ocw.mit.edu online course "A Gentle Introduction to Python" Homework 1 OPT.2 - Secret Messages
    """

    encoded_phrase = ''

    for c in secret_phrase:
        if c.isalpha():
            c_ascii = ord(c) #converts string char to numerical ascii vaule
            c_ascii = c_ascii + shift_value  #shifts the char numerically
            while c.isupper() and c_ascii > 90:  #for uppercase cycles around to beginning of alphabet
                c_ascii -= 26
            while c.islower() and c_ascii > 122: #for lowercase cycles around to beginning of alphabet
                c_ascii -=26
            c = chr(c_ascii)
    
    encoded_phrase = encoded_phrase + c
    return encoded_phrase  

def is_palindrome(test_string):
    test_string = test_string.lower()
    if len(test_string) <= 1:
        return True
    else:
        return test_string[0] == test_string[-1] \
               and is_palindrome(test_string[1:-1])

def pig_latin(word):
    # word is a string to convert to pig-latin
    '''
    Imports a single word and returns the word in pig latin
    '''
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    PREFIX = ['ch','sh','th','st','qu','pl','tr']
    word = (word.strip()).lower()
    vowels = tuple(VOWELS)
    prefix_2_letter = tuple(PREFIX)
    if word.startswith(vowels):
        return word+'hay'
    elif word.startswith(prefix_2_letter):
        return word[2:]+word[:2]+'ay'
    else:
        return word[1:]+word[:1]+'ay'
    
def all_vowels(string_in):
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in string_in if letter.lower() in VOWELS]

def run_pig_latin():
    phrase = ''
    while phrase!='quit':
        phrase = ''
        end_punctuation=''
        pig_phrase = ''
        phrase = raw_input('Please input a phrase or QUIT: ')
        phrase = (phrase.strip()).lower()
        while phrase.endswith(('!','.',',',':',';','?')):
            end_punctuation += phrase[-1]
            phrase = phrase[:-1]
        for word in phrase.split():
            pig_phrase =pig_phrase + pig_latin(word) +' '
        pig_phrase = pig_phrase.strip() + end_punctuation
        print string.capitalize(pig_phrase)
    print 'quitting'
    return None

from collections import Counter

def detect_anagrams(word, test_list):
    return [test for test in test_list if test.lower()!= word.lower() and
            Counter(word.lower()) == Counter(test.lower())]

class Atbash_Cipher:
    """
    Create an implementation of the atbash cipher, an ancient encryption system
    created in the Middle East.

    The Atbash cipher is a simple substitution cipher that relies on
    transposing all the letters in the alphabet such that the resulting
    alphabet is backwards. The first letter is replaced with the last
    letter, the second with the second-last, and so on.

    An Atbash cipher for the Latin alphabet would be as follows:

    ```plain
    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: zyxwvutsrqponmlkjihgfedcba
    ```

    It is a very weak cipher because it only has one possible key, and it is
    a simple monoalphabetic substitution cipher. However, this may not have
    been an issue in the cipher's time.

    Ciphertext is written out in groups of fixed length, the traditional group size
    being 5 letters, and punctuation is excluded. This is to make it harder to guess
    things based on word boundaries.

    ## Examples
    - Encoding `test` gives `gvhg`
    - Decoding `gvhg` gives `test`
    - Decoding `gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt` gives `The quick brown fox jumps over the lazy dog.`
    source: exercism.io  atbash-cipher  readme.md
    Wikipedia [view source](http://en.wikipedia.org/wiki/Atbash)
    """
    def __init__(self):
        alphabet = string.ascii_lowercase
        reverse_alphabet = alphabet[::-1]
        self.key = string.maketrans(alphabet,reverse_alphabet)
        self.remove = string.whitespace + string.punctuation

    def translate(self,phrase):
        #table = makeCipherKey()
        #remove_me = string.whitespace + string.punctuation
        return phrase.lower().translate(self.key, self.remove)
        

    def decode(self,cipher):
        return self.translate(cipher)

    def encode(self,phrase):
        sub_phrase = self.translate(phrase)
        encoded_cipher = ''
        for spaces in range(0,len(sub_phrase),5):
            if (spaces+5)>=len(sub_phrase):
                encoded_cipher =encoded_cipher + sub_phrase[spaces:]
            else:
                encoded_cipher =encoded_cipher + sub_phrase[spaces:spaces+5] + ' ' 
        return encoded_cipher

class Luhn():

    def __init__(self, number=0):
        self.number = number
        self.digits = []
        for x in range(len(str(number))-1,-1,-1):
            self.digits += [int(number // 10**x)]
            number %= 10**x
                
    def addends(self):
        test_digits = self.digits[:]
        odd_even = 0
        for i in range(len(test_digits)-1,-1,-1):
            if  odd_even%2:
                test_digits[i] *= 2
                if test_digits[i] >=10:
                    test_digits[i] -= 9
            odd_even += 1
        
        return test_digits
        
        
    def is_valid(self):
        return not sum(self.addends())%10

    def checksum(self):
        return sum(self.addends())%10

    @staticmethod
    def create(number):
        luhn = Luhn(number*10)
        checksum = luhn.checksum()
        if checksum:
            return number*10 + 10-checksum
        else:
            return number*10

    
