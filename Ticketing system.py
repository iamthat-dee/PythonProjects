# Roller Coaster Ticketing system
print("Hello! Hello! Hello!"
      "\nWelcome to Dee's Ticketing system😁\n"
      "The goal is pretty much simple\n"
      "You input your age and height, Then i'll tell you if you can ride or not/how much you need to pay😇")

height = int(input("What is your Height in cm: "))
age = int(input("What is your Age?: "))

if height >= 150 and age > 5:
    if age > 18:
        bill = 12
        print(f"You can Hop on for the best ride of your life. Adult Tickets are £{bill}, Thank you!🥰")
    elif age <= 18 and age >= 12:
        bill = 7
        print(f"You can Hop on for the best ride of your life. Youth tickets are £{bill}, Thank you!🥰")
    else:
        bill = 5
        print(f"You can Hop on for the best ride of your life. Your Ticket will cost £{bill}, Thank you!🥰")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is £{bill}")
    else:
        print(f"Oh well, Final ticket price is £{bill}")
else:
    print("I'm so sorry, I can't let you ride until you grow taller/older😭\n"
          "My advice is that you eat more beans and come back in a few years😏\n"
          "The advice is free of charge🥰")