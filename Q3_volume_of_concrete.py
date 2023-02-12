play_again = ""

while play_again == "":
    building_type = int(input("Which type of building is this for"
                              " (0 for residential, 1 for commercial):"))
    length = int(input("What length of concrete do you need (in metres):"))
    width = int(input("What width of concrete do you need (in metres):"))

    thickness = 0
    if building_type == 0:
        thickness = 0.25
    else:
        thickness = 0.5

    volume = thickness*length*width
    print(f"The volume of concrete required for a slab with a length of {length}"
          f" and width of {width} a depth of {thickness} is {volume} cubic metres.")

    play_again = input("Would you like to use the program again (Enter to continue, X to leave):").upper()
else:
    print("Thank you for using our program.")
