print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure hidden in my island.")
print("please don't die as i literally have to clean the mess and i don't want to do that!")

start = input("let's start from the main cross road shall we? Y or N: ").upper()
if start == "Y":
    path1 = input('''You have arrived at a crossroad. there are are ☠️ on the the left path and 🍬 on the right side.\nWhat path will you take L or R: ''').upper()
    if path1 == "L":
        print("You stroll down the road like a boss, crushing the bones that lay beneath you")
        path2 = input("You get to a river. Do you swim or wait?: ").upper()
        if path2 == "WAIT":
            print("As a patient person, you take a look around and spot three sweet doors: Red, Blue, Yellow")
            path3 = input("What do you do now, enter W for Wait(W) or D for pick a Door(D)").upper()
            if path3 == "D":
                print("You walk towards the doors majestically")
                path_final = input("What door do you chose, enter R for Red, Y for Yellow or B for Blue").upper()
                if path_final == "B":
                    print("GAME OVER!!!. You were eaten by Beasts🦁. THE END!!!")
                elif path_final == "R":
                    print("GAME OVER!!!. You were burned to ashes by fire 🔥☄️. THE END!!!")
                elif path_final == "Y":
                    print("You open the door to wealth. Congratulations, You WIN!!!")
                else:
                    print("you died a horrible death because you failed to follow simple instructions")
            else:
                print("Game Over!!!. You waited till you grew old and died a natural death. THE END!!!")
        else:
            print('''You were attacked by a school of trout and they took you bum to school. Now you are one of the bones waiting to be steebed on THE END!!!''')
    else:
        print('''you fell into a 🕳 like a retard and died😂. THE END!!!''')
else:
    print('''Good decision to avoid this, Black people don't do treasure hunts, that is assuming you are a black person.THE END!!!''')



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload