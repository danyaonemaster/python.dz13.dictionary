import random

list_cube = [str(random.randint(1, 6)) for _ in range(3)]

print(list_cube)
print(f"""sum numbers :{sum(map(int, list_cube))}
square number : {int("".join(list_cube)) ** 2}""")
