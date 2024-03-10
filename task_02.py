def letters(line, dict):
    if line.__contains__('?'):
        len_input = len(line.replace("?", ""))
        print(f"str len : {len_input}\n"
              f"len even  {dict.get(len_input % 2 + 1)}")
    else:
        print("? missing from line")


dictionary = {1: "Yes", 2: "No"}
should_process = True

while should_process:
    user_input = input("Enter a number: ")

    letters(user_input, dictionary)

    should_process = input("Exit [y/n] : ") == "n"
else:
    print('finish')
