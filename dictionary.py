phone = input('Enter your phone number: ')

digits_mapping={ "1":"one",
                 "2": "two",
                "3":"three",
                "4":"four",
                "5":"five"
                 }
output= ""
for char in phone:
  output += digits_mapping.get(char, " ! ")+ " "
print(output)



message = input('>')
words = message.split(' ')
emojis = {
    ":)":"😊",
    ":(": "😞"
}
output=" "
for word in words:
    output += emojis.get(word, word)
print(output)
