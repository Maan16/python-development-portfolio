#Converting weight from pound to kgs
# weight_in_LBS = input('Please insert your weight in Pounds(LBS): ')
# Converting_in_kg= 0.453592 * int(weight_in_LBS)
# print('Your weight in kg is :' , Converting_in_kg)



Weight = input('Enter your weight:')
unit = input('(L)bs or (k)g:')
unit=unit.upper()

if unit == "K":
    print( f'Your are {int(Weight) *0.2} Pounds ')
elif unit == "L":
    print( f'Your are {int(Weight)/0.2} Pounds ')
else:
    print("Not a valid unit")





