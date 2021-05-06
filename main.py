import string
import random


#Generates variables containing characters as list 

low_list = list(string.ascii_lowercase)
upp_list = list(string.ascii_uppercase)
num_list = list(string.digits)
symb_list = list('!@#$%^&*')


#gets parameters from user and handles password length errors

while True:

    pw_len = int(input("How long do you want your password to be?\nMin: 8\nMax: 50\n>"))

    if pw_len <= 7:
        print ("Password is going to be too short, try again!\n")
        continue
    elif pw_len >= 51:
        print ("Password is going to be overkill, try again!\n")
        continue


#sets final character list contents based on user preferences and handles [Y,N] errors

    else:
        need_num = input("Do you want your password to contain numbers? (Y/N)\n> ").upper()
        need_symb = input("Do you want your password to contain special characters? (Y/N)\n> ").upper()
        
        if need_symb == 'Y' and need_num == 'Y':
            char_list = [low_list, upp_list, num_list, symb_list]
        
        elif need_symb == 'N' and need_num == 'Y':
            char_list = [low_list, upp_list, num_list]
        
        elif need_symb == 'Y' and need_num == 'N':
            char_list = [low_list, upp_list, symb_list]
        
        elif need_symb == 'N' and need_num == 'N':
            char_list = [low_list, upp_list]

        else:
            print ('unknown input(s).Try again!')
            continue


#Password generation

        final_pw = ""
        for i in range(pw_len):

            temp_list = []

            temp_list = random.choice(char_list)
            
            final_pw = final_pw+random.choice(temp_list)

        print("Here is your password:",final_pw)
        
        break
