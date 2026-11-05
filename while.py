# i= 1

# while i<=10:
#  print('   ' *(10-i) + ' * ' * i + ' * ' * (i-1) )
#  i=i+1 
# print('Done')



#Creating guessing game using while
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess=int(input('Guess:'))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break
else:
    print('You Lost!')

