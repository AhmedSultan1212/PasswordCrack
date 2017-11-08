import cs50
import crypt
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: ./crack hash")
        exit(1)
    salt = sys.argv[1][0] + sys.argv[1][1]
    
    for i in range(ord('A'), ord('z') + 1):
        word = chr(i)
        if crypt.crypt(word, salt) == sys.argv[1]:
           print(word)
           exit(0)
        else:
            for j in range(ord('A'), ord('z') + 1):
                word = chr(i) + chr(j)
                if crypt.crypt(word, salt) == sys.argv[1]:
                    print(word)
                    exit(0)
                else:
                    for k in range(ord('A'), ord('z') + 1):
                        word = chr(i) + chr(j) + chr(k)
                        if crypt.crypt(word, salt) == sys.argv[1]:
                            print(word)
                            exit(0)
                        else:
                            for x in range(ord('A'), ord('z') + 1):
                                word = chr(i) + chr(j) + chr(k) + chr(x)
                                if crypt.crypt(word, salt) == sys.argv[1]:
                                    print(word)
                                    exit(0)
    
    exit(1)
                
            
    
    
if __name__ == "__main__":
    main()
