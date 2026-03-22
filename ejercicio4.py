# Ejemplo #4: Escriba un programa que lea un String y un
# caracter y despliegue cuantas ocurrencias del caracter hay
# en el String

user_word = input("Type a word: ")
user_letter = input("Type a letter: ")

count = 0
for letter in user_word:
    if (letter == user_letter):
        count+=1

if (count == 0):
    print("There is no concidences for: ", user_letter)
else:
    print(f"The letter '{user_letter}' appears {count} times in '{user_word}'")