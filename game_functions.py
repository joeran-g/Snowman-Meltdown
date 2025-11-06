def show_snowman(lives):
    parts_of_snowman = [
        "      ___ \n     /___\ ",
        "     (o o)",
        "     ( : ) ",
        "     ( : ) "
    ]
    for amount in range(lives):
        print(f"{parts_of_snowman[amount]}")