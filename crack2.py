import sys

if len(sys.argv) != 2:
    print("Usage: python crack2.py DEShash")
    sys.exit(1)

salt = (sys.argv[1])[0:2:]
f = open(salt)
for line in f:
    h, value = line.split()
    if h == sys.argv[1][2:7:]:
        print("pwd is ", value)
        break
f.close()
    
print("search finished")
