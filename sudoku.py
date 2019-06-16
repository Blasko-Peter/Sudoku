def start_game():
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


if __name__ == "__main__":
    start_game()
