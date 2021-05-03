#importing stuff
import string
import random


#creating variables to store needed ascii chars as string
alph_low = string.ascii_lowercase
alph_upp = string.ascii_uppercase
numeric = string.digits
symb = string.punctuation


#coverting string to list
low_list = list(alph_low)
upp_list = list(alph_upp)
num_list = list(numeric)
symb_list = list(symb)


#getting parameters from user
while True:
    need_num = input("Do you want your password to contain numbers? (Y/N)\n> ").upper()
    need_symb = input("Do you want your password to contain special characters? (Y/N)\n> ").upper()
    pw_len = int(input("How long do you want your password to be?\nMin: 8\nMax: 50\n>"))
    
    

#error handling
    if pw_len <= 7:
        print ("Password is going to be too short, try again")
        continue
    elif pw_len >= 51:
        print ("Password is going to be overkill, try again")
        continue


    #setting final character list contents based on user preferences
    else:
        
        if need_symb == 'Y' and need_num == 'Y':
            char_list = [low_list, upp_list, num_list, symb_list]
        
        elif need_symb == 'N' and need_num == 'Y':
            char_list = [low_list, upp_list, num_list]
        
        elif need_symb == 'Y' and need_num == 'N':
            char_list = [low_list, upp_list, symb_list]
        
        elif need_symb == 'N' and need_num == 'N':
            char_list = [low_list, upp_list]

        else:
            print ('unknown command')


#Password generation
        final_pw = ""
        for i in range(pw_len):

            temp_list = []

            temp_list = random.choice(char_list)
            
            for j in range(1):

                final_pw = final_pw+random.choice(temp_list)

        print("Here is your password:",final_pw)
        
        break
