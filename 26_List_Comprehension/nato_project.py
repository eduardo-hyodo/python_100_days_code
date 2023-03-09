import pandas as pd

df_nato =  pd.read_csv("./nato_phonetic_alphabet.csv")
ditc_nato = { row.letter:row.code for (index,row) in df_nato.iterrows()}
word = input("Give me a word: ").upper()
word_in_letters = list(word)
result = [ ditc_nato[letter] for letter in word]
print(result)
