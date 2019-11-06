def prime(no):
    flag=int(0);
    if(no<3):
        print("Prime")
    else:
        for i in range(2,no/2,1):
            if((no%i)>0):
                flag=1;
    if(flag==0):
        print("Prime")
    else:
        print("Not Prime");            
                

def main():
    no=int(input("Enter no : "));
    prime(no);
  

if __name__=="__main__":
    main();