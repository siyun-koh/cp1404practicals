HEX_COLOUR_CODES = {"aliceblue": "#f0f8ff",
                    "blueviolet": "#8a2be2",
                    "cadetblue1": "#98f5ff",
                    "cornflowerblue": "#6495ed",
                    "darkgreen": "#006400",
                    "darkorchid": "#9932cc",
                    "firebrick": "#b22222",
                    "floralwhite": "#fffaf0",
                    "indianred1": "	#ff6a6a",
                    "khaki1": "#fff68f"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print("The code for colour name \"{}\" is: {}".format(colour_name, HEX_COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ").lower()
