from dogpet import DogPet

def main():
    print("Welcome to 9001VPet – Your Virtual Dog!")
    dog_name = input("Enter your dog’s name: ").strip()
    my_dog = DogPet(dog_name)

    actions = {
        "1": my_dog.feed,
        "2": my_dog.play,
        "3": my_dog.clean,
        "4": my_dog.sleep,
        "5": my_dog.shake_paw,
        "6": my_dog.lie_down
    }
    while True:
        print("\n=== What would you like to do? ===")
        my_dog.show_status()
        print("[1] Feed      [2] Play      [3] Clean")
        print("[4] Sleep     [5] Shake Paw [6] Lie Down")
        print("[0] Quit")
        choice = input("Choose an action: ").strip()
        if choice == "0":
            print(f"Goodbye! See you and {my_dog.name} next time!")
            break
        if choice in actions:
            actions[choice]()
            # after each action, check for game-over
            if my_dog.is_game_over():
                print("\n💔 Oh no! One of your dog's vital stats hit zero.")
                print("Game Over.")
                break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()