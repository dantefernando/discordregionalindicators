def again():
    while True:
        inp = input("\n(Y/N) Would you like to input another sentence? (Y/N)")
        if inp.lower() == "y" or inp.lower() == "yes":
            return 1
        elif inp.lower() == "no" or inp.lower() == "n":
            return 0
        else:
            print("Please input a valid value! E.g. \"y\"")


def convert():
    out = ""
    inp = input("Type sentence to be converted into regional indicator text: ")
    inp = inp.lower()
    for count, letter in enumerate(inp, start=1):
        if letter == " " or letter.isalpha() == False:
            temp = letter
        else:
            if not count == len(out):
                temp = f":regional_indicator_{letter}: "
            else:
                temp = f":regional_indicator_{letter}:"
        out = out + temp
    print(f"#--- OUTPUT ---#\n\n{out}\n\n#------------#\n")

def main():
    while True:
        convert()
        output = again()
        if output == 0:
            break

if __name__ == "__main__":
    main()
