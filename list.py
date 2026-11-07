#Finding the largest number in the list

numbers = [1,2,3,4,5,6,7,8,9,12]
max = numbers[0]
for find in numbers:
     if find > max:
         max=find
print(max)



numbers = [1,2,3,4,5,6,7,8,9,1,2,2,4,5,7,8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
