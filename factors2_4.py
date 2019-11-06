def factorsAdd(no):
    sum=int(0);
    for i in range(0,no,1):
        if (no%i==0):
            sum=sum+i;
    return sum;        

def main():
    no=int(input("Enter no : "));
    print("Factors Addition: ",factorsAdd(no));
  

if __name__=="__main__":
    main();