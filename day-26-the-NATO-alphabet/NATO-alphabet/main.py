import pandas as pd

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_dataframe = pd.read_csv("day-26-the-NATO-alphabet/NATO-alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
phonetic_code_words = [nato_dict.get(letter) for letter in user_input]
print(phonetic_code_words)