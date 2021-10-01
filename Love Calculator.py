# ‼️Don't change the code below 👇🏾
print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# ‼️Don't change the code above 👇🏾

# Write your code below this line

s_name1 = name1.lower()
s_name2 = name2.lower()
f_name = s_name1 + s_name2

love = f_name.count("t") + f_name.count("r") + f_name.count("u") + f_name.count("e")
score = f_name.count("l") + f_name.count("o") + f_name.count("v") + f_name.count("e")

love_score = int(str(love) + str(score))

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")

else:
    print(f"Your score is {love_score}.")


# print(love_score)
