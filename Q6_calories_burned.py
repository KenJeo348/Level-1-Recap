def calorie_calculator():
    CYCLING = 200
    JOGGING = 475
    SWIMMING = 275
    calories_to_kilograms = 0.454/3500

    cycling_time = int(input("How many hours did you cycle:"))
    jogging_time = int(input("How many hours did you jog:"))
    swimming_time = int(input("How many hours did you swim:"))

    calories_burned = CYCLING*cycling_time + JOGGING*jogging_time + SWIMMING*swimming_time

    weight_lost = calories_burned * calories_to_kilograms
    return weight_lost


# Main Routine
yes_no = input("Would you like to calculate how much calories you burned (y for yes, n for no):").lower()

play_again = ""
while play_again != "x":
    if yes_no == "y":
        _weight_lost = calorie_calculator()
        print(f"You have lost {_weight_lost} kilograms")
        play_again = input("Do you want to play again (Enter to continue, x to Exit):").lower()
    else:
        print("Goodbye.")
        play_again = "x"
