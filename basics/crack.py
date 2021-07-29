import sys
import crypt

if len(sys.argv) != 2:
    print("Usage: python crack.py DEShash")
    sys.exit(1)
    
salt = (sys.argv[1])[0:2:]
s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

print("trying 1 simbol passwords")
for c in s:
    if crypt.crypt(c, salt) == sys.argv[1]:
        print("password:",c)
        sys.exit(0)
        
print("trying 2 simbol passwords")
for c2 in s:
    for c1 in s:
        if crypt.crypt(c2+c1, salt) == sys.argv[1]:
            print("password:",c2,end="")
            print(c1)
            sys.exit(0)
            
print("trying 3 simbol passwords")
for c3 in s:
    for c2 in s:
        for c1 in s:
            if crypt.crypt(c3+c2+c1, salt) == sys.argv[1]:
                print("password:", c3, end="")
                print(c2,end="")
                print(c1)
                sys.exit(0)
              
print("trying 4 simbol passwords")
for c4 in s:
    for c3 in s:
        for c2 in s:
            for c1 in s:
                if crypt.crypt(c4+c3+c2+c1, salt) == sys.argv[1]:
                    print("password:", c4, end="")
                    print(c3, end="")
                    print(c2, end="")
                    print(c1)
                    sys.exit(0)     

print("trying 5 simbols passwords")
for c5 in s:
    for c4 in s:
        for c3 in s:
            for c2 in s:
                for c1 in s:
                    if crypt.crypt(c5+c4+c3+c2+c1, salt) == sys.argv[1]:
                        print("password:", c5, end = "")
                        print(c4, end = "")
                        print(c3, end = "")
                        print(c2, end = "")
                        print(c1)
                        sys.exit(0)

print("can't crack this hash")
