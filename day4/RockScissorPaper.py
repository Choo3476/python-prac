import random
import parameter

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
computer = random.randint(0,2)

game_image = [parameter.rock, parameter.paper, parameter.scissor]

print(game_image[player])
    
print('Computer Chose:')

print(game_image[computer])

# 플레이어가 바위인 경우
if (player == 0) and (computer == 1):
    print('You lose!')
elif (player == 0) and (computer == 2):
    print('You Win!')
elif (player == 0) and (computer == 0):
    print('Draw')

# 플레이어가 보인 경우
if player == 1 and computer == 2:
    print('You lose!')
elif player == 1 and computer == 0:
    print('You Win!')
elif player == 1 and computer == 1:
    print('Draw')

# 플레이어가 가위인 경우
if player == 2 and computer == 0:
    print('You lose!')
elif player == 2 and computer == 1:
    print('You Win!')
elif player == 2 and computer == 2:
    print('Draw')