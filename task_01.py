import random

cube_1 = str(random.randint(1, 6))
cube_2 = str(random.randint(1, 6))
cube_3 = str(random.randint(1, 6))

print(cube_1, cube_2, cube_3)
print(f"""sum numbers :{sum(map(int, [cube_1, cube_2, cube_3]))}
square number : {int(cube_1 + cube_2 + cube_3) ** 2}""")
