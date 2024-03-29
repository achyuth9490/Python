# importing module
import re

# taking input from user
n = int(input())

# iterating through the credit cards
for t in range(n):
    
    #taking the credit card number from user
    credit = input().strip()
    credit_removed_hiphen = credit.replace('-','')
    
    # valid is true in the beggining
    valid = True
    
    # using regual expressions
    length_16 = bool(re.match(r'^[4-6]\d{15}$',credit))
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))    
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',credit_removed_hiphen))
    
    # checking if the above regural expressions are true
    if length_16 == True or length_19 == True:
        if consecutive == True:
            valid=False
    else:
        valid = False       
    if valid == True:
        print('Valid')
    else:
        print('Invalid')