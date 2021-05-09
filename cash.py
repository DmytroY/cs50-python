def main():
    while True:
        s = input("Change owed:")
        try:
            fl = float(s)
            if fl > 0:
                c = 0
                while fl >= 0.25:
                    fl = round(fl - 0.25, 2)
                    c = c + 1

                while fl >= 0.1:
                    fl = round(fl - 0.1, 2)
                    c = c + 1            

                while fl >= 0.05:
                    fl = round(fl - 0.05, 2)
                    c = c + 1

                while fl >= 0.01:
                    fl = round(fl - 0.01, 2)
                    c = c + 1

                print(c)
                return(0)
    
        except:
            pass
        
        
main()
