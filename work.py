import random
count_user=0
count_comp=0



def get_user_choice():
    user_choice = input("Выберите: камень, ножницы бумага спок или ящерица? ").lower()
    while user_choice not in ['камень', 'ножницы', 'бумага', 'спок', 'ящерица']:
        print("Неверный ввод. Пожалуйста, выберите камень, ножницы,спок или ящерица.")
        user_choice = input("Выберите: камень, ножницы,бумага, спок или ящерица? ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага', 'спок', 'ящерица'])

def determine_winner(user_choice, computer_choice):
    global count_user
    global count_comp
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
 (user_choice == 'камень' and computer_choice == 'ножницы') or
 (user_choice == 'ножницы' and computer_choice == 'бумага') or
 (user_choice == 'бумага' and computer_choice == 'камень') or
 (user_choice == 'камень' and computer_choice == ' ящерица')or
 (user_choice == 'ящерица' and computer_choice == 'спок') or
 (user_choice == 'спок' and computer_choice ==  'ножницы') or
 (user_choice == 'ножницы' and computer_choice == 'ящерица') or
 (user_choice == 'ящерица' and computer_choice == 'бумага') or
 (user_choice == 'бумага' and computer_choice ==  'спок') or
 (user_choice == 'спок' and computer_choice == 'камень')


    ):
        count_user+=1
        return f"Вы выиграли! У Вас {count_user} очков"
    else:
        count_comp+=1
        return f"Вы проиграли. У компьютера {count_comp} очков"


def game():
    print("Добро пожаловать в игру 'камень, ножницы, бумага, спок, ящерица'!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if count_user == 3 or count_comp == 3:
            print("Спасибо за игру! До свидания.")
            break
       # play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
        #if play_again != 'да':
           # print("Спасибо за игру! До свидания.")
           # break

game()
