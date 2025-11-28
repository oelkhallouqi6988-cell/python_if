

fruits=["pomme", "banane", "cerise"]

for index, fruit in enumerate(fruits):
    print(f"{index} → {fruit}")

for index, fruit in enumerate(fruits, start=1):
    print(f"{index} → {fruit}")



