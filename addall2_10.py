def add(no):
    sum=int(0)
    for i in str(no):
        sum=sum+int(i);
    return sum



def main():
    no=int(input("Enter no : "));
    print("Sum is: ",add(no))
  

if __name__=="__main__":
    main();