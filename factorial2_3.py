def factorial(no):
    fact=int(1);
    for i in range(1,no+1):
        fact=fact*i;
    return fact    

def main():
    no1=int(input("Enter no : "));
    print("Factorial: ",factorial(no1));
  

if __name__=="__main__":
    main();