import random

answer = input('Guess our secret number! ')

num = (random.randint(0, 1001))

while not answer.isnumeric():
    answer = input('Oh no, that didn\'t work! Guess our secret number!: ')

while True:
  if int(answer) == num:
    break
  elif int(answer) > num:
    print('Too big!')
  elif int(answer) < num:
      print('Too small!')
  answer = input('Try again: ')
print('Correct!')