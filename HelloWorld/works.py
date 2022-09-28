#Weight Converter

weight = int(input("Enter your Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    convertedW = weight * 0.45
    print(f"You are {convertedW} kilos")
else:
    convertedW = weight / 0.45
    print(f"You are {convertedW} pounds")
