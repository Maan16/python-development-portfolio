# def greet_user():
#     print("Welcome to the new function")
#     print("This is my first function in Python")
#
# greet_user()

# def greet_user(first_name, last_name):
#     print(f'Welcome to the new function: {first_name} {last_name}!')
#     print("This is my first function in Python")
#
# greet_user ("John", "Smith") #key word argumnets


message = input('>')
def emojis_pot(message):
    words = message.split(' ')
    emojis = {
    ":)":"😊",
    ":(": "😞"
                }
    output=" "
    for word in words:
         output += emojis.get(word, word) + " "

    return output

print(emojis_pot(message))