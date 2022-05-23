import random

print("Welcome to Password Generator!!!")
print("This simple program is created by Shaptus!!")

# A variable that accepts user input of the number of passwords to genereate.
while True:
  try:
    numberOfPasswords = int(input("Enter the number of passwords to generate: "))
    break
  except:
    print("User input must  be a  number!!!")
    
# A variable that accepts user input of the number of characters the password should  have.
while True:
  try:
    numberOfCharacters = int(input("Enter the number of characters in a password: "))
    break
  except:
    print("User inputer must be a number!!!")

# A string of alphabetic characters to be used in the generation of the password.
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_-=+\|,<.>/?\|;:[]{}/*-+"

print("Here are your randomly generated password(s): ")

# A for statement for the generation of the passwords.
for pwd in range(numberOfPasswords):
  passwords = ""
  for i in range(numberOfCharacters):
    passwords += random.choice(chars)
  print(passwords)
    