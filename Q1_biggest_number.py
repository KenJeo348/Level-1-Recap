first_number = int(input("Enter First Number:"))
second_number = int(input("Enter Second Number:"))

if first_number == second_number:
    print("Numbers are equal.")
elif first_number >= second_number:
    print(f"{first_number} is bigger")
else:
    print(f"{second_number} is bigger")
