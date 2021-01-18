def again():
    while True:
        inp = input("\n(Y/N) Would you like to input another sentence? (Y/N)")
        if inp.lower() == "y" or inp.lower() == "yes":
            return False  # Don't exit the program
        elif inp.lower() == "no" or inp.lower() == "n":
            return True  # Exit the program
        else:
            print("Please input a valid value! E.g. \"y\"")


def out(temp):
    print(f"#--- OUTPUT ---#\n\n{temp}\n\n#------------#\n")


def isLast(tempChar, count, inp):
    if not count == len(inp):  # If char is not in the last index of the str
        temp = f"{tempChar} "
    else:  # If char is in the last index of the string don't give it an extra space
        temp = f"{tempChar}"
    return temp


def digit_to_word(letter):
    dictionary = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
                  "8": "eight", "9": "nine", "0": "zero"}
    word = dictionary[letter]
    letter = word
    return letter


def convert():
    tempOut = ""
    inp = input("Type sentence to be converted into regional indicator text: ")
    for count, letter in enumerate(inp.lower(), start=1):
        if letter.isnumeric():  # If char is an integer
            word = digit_to_word(letter)
            tempChar = f":{word}:"
        # elif letter == " " or letter.isalpha() == False:  # If char is a space or not alphabet
        elif letter.isalpha():  # If char is a letter in the alphabet
            tempChar = f":regional_indicator_{letter}:"
        else:  # Char is not a letter or a number
            tempChar = letter

        temp = isLast(tempChar, count, inp)  # If it's the last char don't add a space to the end
        tempOut += temp
    return tempOut


def main():
    while True:
        temp = convert()
        out(temp)
        response = again()
        if response == 1:  # Exit == True
            break


if __name__ == "__main__":
    main()
