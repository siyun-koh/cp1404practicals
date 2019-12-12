HEX_COLOUR_CODES = {"AliceBlue": "#f0f8ff",
                    "BlueViolet": "#8a2be2",
                    "CadetBlue1": "#98f5ff",
                    "CornflowerBlue": "#6495ed",
                    "DarkGreen": "#006400",
                    "DarkOrchid": "#9932cc",
                    "firebrick": "#b22222",
                    "FloralWhite": "#fffaf0",
                    "IndianRed1": "	#ff6a6a",
                    "khaki1": "#fff68f"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is: {}".format(colour_name, HEX_COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
