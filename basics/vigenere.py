# encripting message with Vigenere chipfer

import sys

def shift(c):
    if c.islower():
        return ord(c)-97
    if c.isupper():
        return ord(c)-65    
    sys.exit(3)

def main():
    if len(sys.argv) != 2:
        print("Usage: python vigenere.py keyword")
        sys.exit(1)
    
    keyword = sys.argv[1]
    if keyword.isalpha() != True:
        print("Usage: python vigenere.py keyWORD")
        sys.exit(2)
    
    text = input("plaintext: ")
    print("ciphertext: ",  end="")
    
    # Counter for keyword characters
    i=0
    # processing of message characted by character
    for c in text:
        # reset keyword couner in case of keyword finished
        if i >= len(keyword):
            i=0
        # is not letter
        if ord(c) not in range(0x41,0x5b) and ord(c) not in range(0x61,0x7b):
            ord_cc = ord(c)
        #is letter
        else:
            ord_cc = ord(c)+ shift(keyword[i])
    
            # Uppercase
            if ord(c) <= 0x005a and ord_cc > 0x005a:
                ord_cc -=26
        
            # Lowercase
            if ord_cc > 0x7a:
                ord_cc -=26
            i = i + 1
        # print encripted character        
        print(chr(ord_cc), end="")
        
    print()
    
    
if __name__ == "__main__":
    main()
