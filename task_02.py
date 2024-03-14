def linter(line, in_dict):
    if not line.__contains__('?'):
        print("The question mark is missing in the line")
        return

    len_input = len(line.replace("?", ""))
    print(in_dict.get(len_input % 2 + 1))


dictionary = {1: "Yes", 2: "No"}
while True:
    user_input = input("Enter a question sentence: ")
    linter(user_input, dictionary)
    if input("Try again? [y/n] : ") == "n":
        break

print('finish')
