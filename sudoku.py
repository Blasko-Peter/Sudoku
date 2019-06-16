def start_game():
    the_table = database()
    index = 0
    difficult_level = 0
    while index < 1:
        difficult = input("Válassz nehézséget (1-3): ")
        if difficult in ['1', '2', '3']:
            difficult_level = difficult
            index += 1
        else:
            print("Hibás nehézségi szint!")
    print(difficult_level)


def database():
    table = [
            ['4', '3', '9', '8', '6', '7', '2', '5', '1'],
            ['1', '7', '8', '5', '4', '2', '6', '3', '9'],
            ['6', '5', '2', '9', '3', '1', '8', '4', '7'],
            ['7', '4', '3', '1', '9', '8', '5', '6', '2'],
            ['5', '2', '6', '4', '7', '3', '1', '9', '8'],
            ['8', '9', '1', '6', '2', '5', '4', '7', '3'],
            ['3', '1', '7', '2', '5', '4', '9', '8', '6'],
            ['9', '8', '4', '3', '1', '6', '7', '2', '5'],
            ['2', '6', '5', '7', '8', '9', '3', '1', '4']
            ]
    return table


if __name__ == "__main__":
    start_game()
