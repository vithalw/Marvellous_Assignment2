def add(no1,no2):
    return no1+no2;
def sub(no1,no2):
    return no1-no2;
def mult(no1,no2):
    return no1*no2;
def div(no1,no2):
    return no1/no2;


def main():
    no1=int(input("Enter no 1: "));
    no2=int(input("Enter no 2: "));
    print("Addition: ",add(no1,no2));
    print("Subtraction: ",sub(no1,no2));
    print("Multiplication: ",mult(no1,no2));
    print("Division: ",div(no1,no2));
    
  

if __name__=="__main__":
    main();