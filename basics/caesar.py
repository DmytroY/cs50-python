import sys

if len(sys.argv) != 2:
    print("Usage: python caesar.py Number")
    sys.exit(1)
    
shift = int(sys.argv[1])%26

text = input("plaintext: ")
print("ciphertext:",  end="")

for c in text:
    # is not letter
    if ord(c) not in range(0x41,0x5b) and ord(c) not in range(0x61,0x7b):
        ord_cc = ord(c)
    #is letter
    else:
        ord_cc = ord(c)+ shift
    
        # Uppercase
        if ord(c) <= 0x005a and ord_cc > 0x005a:
            ord_cc -=26
        
        # Lowercase
        if ord_cc > 0x7a:
            ord_cc -=26
    
    print(chr(ord_cc), end="")
print()
