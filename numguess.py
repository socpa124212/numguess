from random import randint

# create answer range : 1 to 100 (integer)
answer = randint(1,100)

# print answer(for debugging)
print(answer)

# get user's name, guess
user_name = input("hello, there! what is your name?")
guess = input(f'Hi, {user_name} guess the number between 1 ~ 100 : ')

# print to check
print(user_name, guess)
