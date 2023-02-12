SOUND_SPEED = 340
play_again = ""
while play_again != "x":
    thunder_lightning_interval = int(input("Time between lightning and thunder, (in seconds):"))
    storm_distance = thunder_lightning_interval * SOUND_SPEED

    print(f"The storm is {storm_distance}m away.")
    play_again = input("Would you like to play again, (Press any key to play, x to Exit):").lower()
