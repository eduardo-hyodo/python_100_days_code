import pandas as pd

df_nato =  pd.read_csv("./nato_phonetic_alphabet.csv")
ditc_nato = { row.letter:row.code for (index,row) in df_nato.iterrows()}
def generate_phonetic():
    word = input("Give me a word: ").upper()
    word_in_letters = list(word)
    try:
        result = [ ditc_nato[letter] for letter in word]
    except KeyError as key_error_message:
        print("User only letters")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
