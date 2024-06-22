"""
CP1404/CP5632 Practical
Use constant dictionary to return hex colour code
"""

COLOUR_TO_HEX_CODE = {"Red": "#ff0000", "Green": "#00ff00", "Blue": "#0000ff", "Dark Brown": "#654321",
                      "Gray": "bebebe", "Aqua": "00fff", "Lilac": "#c8a2c8", "Mint": "#3eb489", "Mustard": "#ffdb58",
                      "Ruby": "#e0115f"}

colour = input("Enter colour: ").title()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX_CODE[colour])
    except KeyError:
        print("Invalid colour entered.")
    colour = input("Enter colour: ")
