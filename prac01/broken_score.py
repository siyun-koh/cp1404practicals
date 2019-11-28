"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
# old code
"""score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""
# new code
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score!")
elif score >= 90:
    print("Excellent!")
elif score >= 50:
    print("Passable.")
elif score < 50:
    print("Bad.")
