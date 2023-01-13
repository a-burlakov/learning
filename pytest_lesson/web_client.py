def create_phone_number():
    n = [str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    return f'({"".join(n[:3])}) {"".join(n[3:6])}-{"".join(n[6:])}'

print(create_phone_number())
