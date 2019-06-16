import random


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
    game_table = create_game_table(the_table, difficult_level)
    play_game(the_table, game_table, difficult_level)


def create_game_table(the_table, difficult_level):
    for i in range(0, len(the_table)):
        numbers = set()
        while len(numbers) < (int(difficult_level) * 2) - 1:
            number = random_int(0, 8)
            numbers.add(number)
        for num in numbers:
            the_table[i][num] = " "
    return the_table
    

def random_int(start, end):
    number = random.randint(start, end)
    return number


def play_game(the_table, game_table, difficult_level):
    number_of_space = ((int(difficult_level) * 2) - 1) * 9
    while number_of_space > 0:
        print_table(game_table)
        actual_row = check_character("Adja meg a sor betűjelét (A-I): ")
        actual_column = check_number("Adja meg az oszlop számát (1-9): ")
        actual_number = check_number("Adja meg a kívánt számot (1-9): ")
        print(actual_row)
        print(actual_column)
        print(actual_number)


def check_character(question):
    characters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}
    index = 0
    actual_row_number = 9
    while index < 1:
        character = input(question)
        if character in characters:
            actual_row_number = characters.get(character)
            index += 1
        elif(character == 'q'):
            exit()
        else:
            print("Hibás karakter!")
    return actual_row_number


def check_number(question):
    index = 0
    actual_number = 0
    while index < 1:
        number = input(question)
        if number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            actual_number = number
            index += 1
        else:
            print("Hibás szám!")
    return actual_number


def print_table(game_table):
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    print("    1 2 3   4 5 6   7 8 9 ")
    print("  =========================")
    for i in range(0, len(game_table)):
        print('%s | %s %s %s | %s %s %s | %s %s %s |' % (
                rows[i], game_table[i][0], game_table[i][1], game_table[i][2], game_table[i][3], game_table[i][4],
                game_table[i][5], game_table[i][6], game_table[i][7], game_table[i][8]))
        if i % 3 == 2:
            print("  =========================")


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
