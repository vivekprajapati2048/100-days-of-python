PLACEHOLDER = "[name]" 

with open("Input/Names/invited_names.txt") as inv_names:
    invited_names = [name.strip() for name in inv_names.readlines()]

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    for name in invited_names:
        updated_letter = letter_content.replace(PLACEHOLDER, name)

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(updated_letter)
            print(f"letter for {name} saved!")



    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp