
# 1st function: prints message 
print('have a nice day!😘')

#2nd fuction: asks for the dog's name and prints it
dog_name = input(' What is your dog name? ')
print(dog_name)

#3rd function: asks for the users age and checks if they are old enough to buy beer
age = int(input('how old are you? '))
if age >= 18:
  print('ok, i can sell you this beer ')
else:
  print('go out, you are too young')

#4th function: finds the max and min numbers in a list
random_num = [23, 56, 73, 444, 12, 37]

print(max(random_num))
print(min(random_num))

#5th NEW function "round()": rounds the number to the nearest integer
print(round(6.8))
