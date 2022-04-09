"""
author =
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

'''variable settings'''
users = {"bob": "123",                                                # user dictionary declaration
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}
separator = "-"*45

'''login to app'''
user = input("username: ")
password = input("password: ")
if not len(user) or not len(password) or not users.get(user) == password:        # empty entry and login checking
    print("Unregistered user, terminating the program...")
    quit()
else:
    print(f"{separator}\nWelcome to the app, {user}.\nWe have {len(TEXTS)} texts to be analysed.\n{separator}")

'''Text selection'''
text_selection = input(f"Enter a number between 1 and {len(TEXTS)} to select text for analysis: ")
print(separator)
# empty entry + validity checking
if not len(text_selection) or not text_selection.isdigit() or not 1 <= int(text_selection) <= len(TEXTS):
    print("Wrong selection, terminating the program...")
    quit()

'''Text analysis'''
words = TEXTS[int(text_selection)-1].split()                # list of words from TEXT
clear_words = [(word.strip(".,")) for word in words]        # excluding ".," from word
word_no = len(words)                                        # count of words
titlecase_no, uppercase_no, lowercase_no, numeric_no, numeric_sum = 0, 0, 0, 0, 0
for word in clear_words:
    if word.istitle():                                      # No of titlecase strings
        titlecase_no += 1
    if word.isupper() and not word[0].isdigit():            # No of uppercase strings
        uppercase_no += 1
    if word.islower():                                      # No of lowercase strings
        lowercase_no += 1
    if word.isnumeric():                                    # No of numeric strings words and sum of numbers
        numeric_no += 1
        numeric_sum += int(word)

print(f"There are {word_no} in the selected text.",
      f"There are {titlecase_no} titlecase words.",
      f"There are {uppercase_no} uppercase words.",
      f"There are {lowercase_no} lowercase words.",
      f"There are {numeric_no} numeric strings",
      f"The sum  of all numbers is {numeric_sum}.",
      sep="\n")

"""bar chart"""
clear_words_length = sorted([len(word) for word in clear_words])            # sorted list of word length
clear_words_length_set = set(clear_words_length)                            # unique word length
max_length = max(clear_words_length_set)
result_dict = {length: clear_words_length.count(length) for length in clear_words_length_set}
just = 4                                                # parameter for formated bar char print
if len(str(max_length)) >= 2:
    just = len(str(max_length)) + 2
max_occurr = 11                                         # parameter for formated bar char print
if max(result_dict.values()) >= 11:
    max_occurr = max(result_dict.values())
separator_bar = "-" * (max_occurr + just * 2 + 3)
print(separator_bar)
print("LEN|".rjust(just), "OCCURRENCES".center(max_occurr), "| NR.")
print(separator_bar)
for word in clear_words_length_set:
    print(f"{word}|".rjust(just), ("*"*result_dict.get(word)).ljust(max_occurr), "|", str(result_dict.get(word)))
