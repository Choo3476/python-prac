print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88         8PP""""""" 
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"'
                                                                           
                                                                           
                                                               
88           88                                 88  
""           88                                 88  
             88                                 88  
88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8 
''')

print('Welcome to Treasure island.')
print('Your mission is to find the treasure.')

direction = input("You're at a cross road. Where do you want to go?\n      Type 'left' or 'right'\n")
if direction == 'right':
    print("Game Over")
else:
    action = input("You're at a river. What you want to do?\n      Type 'swim' or 'wait'\n")
    if action == 'swim':
        print("Game Over")
    else:
        door = input("You're on the doors. where do you want to enter?\n      Type 'Red' or 'Blue' or 'Yellow'\n")
        if door == 'Red':
            print("Game Over")
        elif door == 'Blue':
            print("Game Over")
        else:
            print("You Win!")
