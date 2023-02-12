PI = 3.14
play_again = ""

while play_again != "x":
    radius = int(input("What is the radius of the sphere, (in centimetres):"))
    area = 4 * PI * radius**2
    volume = 4/3 * PI * radius**3

    print(f"The area of the sphere is {area}, and the volume of the sphere is {volume}.")

    play_again = input("Would you like to use the program again, (Any key to continue, x to Exit):")
