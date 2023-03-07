with open("./Input/Letters/starting_letter.txt") as f_starting_letter:
    starting_letter = f_starting_letter.read()
with open("./Input/Names/invited_names.txt") as f_invited_names:
    names =  f_invited_names.read().splitlines()
    for name in names:
        new_letter =  starting_letter.replace("[Name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_letter:
            output_letter.write(new_letter)

