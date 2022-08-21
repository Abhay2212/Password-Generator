import string
import random
from unicodedata import digit 
# Characters to Generate Password from
alphabets = list(string.ascii_letters)
digit = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()" )

def generate_random_password():
    # length of the password from the user
    length = int(input("Enter the Password length : ")) 
     
    # number of character types 
    alphabets_count = int(input("Enter Alphabets count in Password :"))
    digit_count = int(input("Enter Digit count in Password :"))
    special_characters_count = int(input("Enter Special Characters count in Password :"))

    characters_count =  alphabets_count +  digit_count +  special_characters_count

    # check the total length with characters sum count
    if characters_count > length:
        print ("Characters total count is greater than the password length")
        return

    # initializing the password
    password = []

    # picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    # picking random digits    
    for i in range(digit_count):
        password.append(random.choice(digit))

    # picking random alphabets
    for i in range(special_characters_count) :
        password.append(random.choice(special_characters))


    # if the total character count is less than the password length
    # add random character to make it equal to te length
    if characters_count < length :  
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))


    # shuffeling the resultent password 
    random.shuffle(password)       

    # printng the list
    print("".join(password))



# invoking the function
generate_random_password()

