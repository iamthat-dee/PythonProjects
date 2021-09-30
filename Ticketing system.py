# Roller Coaster Ticketing system
print("Hello! Hello! Hello!"
      "\nWelcome to my very Daniel's Ticketing system😁\n"
      "The goal is pretty much simple\n"
      "You give me your age and height, Then i'll tell you if you can ride or not/how much you need to pay😇")

height = int(input("What is your Height in cm: "))
age = int(input("What if your age?: "))

if height >= 120 and age > 5:
    if age > 18:
        print("You can Hop on for the best ride of your life. Your Ticket will cost £12, Thank you!🥰")
    elif age <= 18 and age >= 12:
        print("You can Hop on for the best ride of your life. Your Ticket will cost £7, Thank you!🥰")
    else:
        print("You can Hop on for the best ride of your life. Your Ticket will cost £5, Thank you!🥰")
else:
    print("I'm so sorry, I can't let you ride until you grow taller/older😭\n"
          "My advice is that you eat more beans and come back in a few years😏\n"
          "The advice is free of charge🥰")