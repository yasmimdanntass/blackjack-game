import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                                      
os.system('clear')

user = []
computer = []
def draw(x):
    x.append(cards[random.randint(0, 12)])
def replaceace():
        index = user.index(11)
        user[index] = 1    
# asking the user if they want to play
def bj():
    ui = input('HEY! WOULD YOU LIKE TO PLAY A GAME OF BLACKJACK? ')
    if ui == 'y':
        os.system('clear')
        print(logo)
        for i in range(2):
            draw(user)
            draw(computer)
        # printing the user's and the computer's cards
        print(f'    Your cards: {user}, total score: {sum(user)}')
        if (10 and 11) in user:
            print(f"    Computer's cards: {computer}")
            if 10 and 11 in computer:
                print('YOU LOSE! COMPUTER HAS A BLACKJACK!')
            else:
                print('YOU WON! YOU HAVE A BLACKJACK!')
        elif sum(user) > 21:    
            if 11 in user:
                replaceace()
                if sum(user) > 21:
                    print(f"    Computer's cards: {computer}")
                    print('YOU LOSE! YOU WENT OVER!')
            else:
                print(f"    Computer's cards: {computer}")
                print('YOU LOSE! YOU WENT OVER!')
        else:
            print(f"    Computer's first card: {computer[0]}")
            while True:
                ask = input('Would you like to draw another card? ')
                if ask == 'y':
                    draw(user)
                    print(f'    Your cards: {user}, total score: {sum(user)}')
                    if sum(user) > 21:
                        print(f"    Computer's cards: {computer}")
                        print('YOU LOSE! YOU WENT OVER!')
                        break
                    else:
                        print(f"    Computer's first card: {computer[0]}")
                elif ask == 'n':
                    while sum(computer) < 17:
                        draw(computer)
                    if sum(computer) > 21:
                        print(f'    Your cards: {user}, total score: {sum(user)}')
                        print(f"    Computer's cards: {computer}")
                        print("COMPUTER WENT OVER! YOU WIN!")
                        break
                    else:
                        print(f'    Your cards: {user}, total score: {sum(user)}')
                        print(f"    Computer's cards: {computer}")
                        if 21 - sum(computer) > 21 - sum(user):
                            print('YOU GOT CLOSER! YOU WON!')
                        elif 21 - sum(user) > 21 - sum(computer):
                            print('COMPUTER GOT CLOSER! YOU LOSE :(')
                        else:
                            print("IT'S A DRAW!")
                        break
    user.clear()
    computer.clear()
    bj()
                    
bj()
            


            

