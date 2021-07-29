def luhn(number):
    s_even=0
    s_odd=0
    l = len(number)
    n = number[::-1]
    
    # evens (парні)
    for i in range(1,l,2):
        if int(n[i]) < 5:
            s_even = s_even + int(n[i])*2
        else:
            s_even = s_even + int(n[i])*2-9
            
    # odds (непарні)
    for i in range(0,l,2):
        s_odd = s_odd + int(n[i])

    # check for multiplicity 10
    if (s_even + s_odd) % 10 == 0:
        return True
    else:
        return False

def main():
    while True:
        s = input("Number:")
        try:
            i = int(s)
            card ="INVALID"

            # define card type by start numbrs and lenght
            if( s[0:2] == "34" or s[0:2] == "37"):
                if len(s) == 15:
                    card = "AMEX"
            
            if int(s[0:2]) >= 51 and int(s[0:2]) <= 55:
                if len(s) == 16:
                    card = "MASTERCARD"

            if s[0] == "4":
                if len(s) == 13 or len(s) == 16:
                    card = "VISA"                    
            
            # chek card number corectness with Luhn algorithm
            if luhn(s) == True:
                print(card)
            else:
                print("INVALID")
            return(0)
        except:
            pass
    
    
if __name__ == "__main__":
    main()
