

guess = 0 
tries = 0
tries_limit = 3

while guess != 6 and tries < tries_limit:
    guess = int(input('Guess the number: '))
    tries=tries+1
    if guess == 6:
        print('You got it!')
    elif tries < 3:
        print('You still got ',tries_limit-tries, ' left')
    else:
        print('Out of tries! The number was 6😬 ')



