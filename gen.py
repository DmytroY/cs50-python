# Generate hash table for up to 3 simbol password. DES, salts are 50,51,61
import crypt

salts = ["50", "51", "61"]
s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

for salt in salts:
    f = open(salt, "a")
    print("Generate hash tables for salt ", salt)
    print("for 1 simbol passwords.....", end="")
    for c1 in s:
        pwd = c1
        hsh = crypt.crypt(pwd, salt) 
        r_hash = hsh[2:7:]
        f.write(r_hash + " " + pwd + "\n")
    print("Done")
    
    print("for 2 simbol passwords.....", end="")    
    for c2 in s:
        for c1 in s:
            pwd = c2 + c1
            hsh = crypt.crypt(pwd, salt) 
            r_hash = hsh[2:7:]
            f.write(r_hash + " " + pwd + "\n")
    print("Done")

    print("for 3 simbol passwords.....", end="")    
    for c3 in s:
        for c2 in s:
            for c1 in s:
                pwd = c3 + c2 + c1
                hsh = crypt.crypt(pwd, salt) 
                
                r_hash = hsh[2:7:]
                f.write(r_hash + " " + pwd + "\n")
    print("Done")
    
    print("Done for salt", salt)    
    f.close()
print("Finished")
