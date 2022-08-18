NAME_TO_CODE = {"AntiqueWhite": "#faebd7", "Arylide Yellow": "#e9d66b", "Bittersweet": "#fe6f5e",
                "BlueViolet": "#8a2be2",
                "Bronze": "#cd7f32", "CadetBlue": "#5f9ea0", "Canary Yellow": "#ffef00", "Carnation Pink": "#ffa6c9",
                "Carrot Orange": "#ed9121", "Coquelicot": "#ff3800"}
print(NAME_TO_CODE)

colour_name = input("Enter the colour name: ")
while colour_name != " ":
    if colour_name in NAME_TO_CODE:
        print("{}'s code is {}".format(colour_name, NAME_TO_CODE[colour_name]))
    else:
        print("Invalid short colour")
    colour_name = input("Enter the colour name: ")

