import csv
import sys


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py <database file> <person sequence file>")
        
    # open dna database file
    db = []
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)  # <csv.DictReader object at 0x7f372fd9aee0>
        header = reader.fieldnames  # read header only for get list of markers ['name', 'AGATC', 'AATG', 'TATC']
        for row in reader:
            db.append(row)        # [{'name': 'Alice', 'AGATC': '2', 'AATG': '8', 'TATC': '3'}, {'name': 'Bob',  ....
        f.close()
        
        header.pop(0)               # remove 'name' from header ['AGATC', 'AATG', 'TATC']

    # open a person dna sequence file
    with open(sys.argv[2], newline='') as f:
        s = f.read()   # 'AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAAT....
        f.close()
    
    # find longest Short Tandem Repeats, for example {'AGATC': 4, 'AATG': 1, 'TATC': 5}
    counts = {}
    for i in range(len(header)):
        sample = header[i]
        count = 0
        while True:
            if s.find(sample) < 0:
                break
            else:
                sample = sample + header[i]
                count = count + 1
        counts.update({header[i]: count}) 

    # compare counts and db
    for l in range(len(db)):
        flag = 1
        for i in range(len(header)):
            #s1 = int(db[l][header[i]])
            s2 = counts[header[i]]
            if int(db[l][header[i]]) != counts[header[i]]:
                flag = 0
        if flag == 1:
            print(db[l]['name'])
            return
    print("No match")


if __name__ == "__main__":
    main()
