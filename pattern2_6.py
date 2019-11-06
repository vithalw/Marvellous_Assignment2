def pattern(no):
    for i in range(0,no,1):
        for j in range(i,no,1):
            print("*",end=" ");
        print("");    



def main():
    no=int(input("Enter no : "));
    pattern(no);
  

if __name__=="__main__":
    main();