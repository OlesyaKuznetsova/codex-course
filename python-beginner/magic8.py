# a magic8.py program that can respond to any Yes or No questions 
#  with a different answer each time it executes

import random

question = input('Question: ')

random_num = random.randint(1, 9)

if random_num == 1:
  print('Yes - definitely.')
elif random_num == 2:
  print('It is decidedly so.')
elif random_num ==3:
  print('Without a doubt.')
elif random_num == 4:
  print('Reply hazy,try again.')
elif random_num == 5:
  print('Ask again later.')
elif random_num == 6:
  print('Better not tell you now.')
elif random_num == 7:
  print('My sources say no.')
elif random_num == 8:
  print('Outlook not so good.')
else:
  print('Very doubtful.')
