import game_logic as game


def main():
    while True:
        game.play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            continue
        break


if __name__ == "__main__":
    main()