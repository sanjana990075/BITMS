class prime:
    def cal(self,num):
        for i in range(2,num):
            if(num%i==0):
                flag=1  # This flag variable is local to the loop, it won't be accessible outside the loop.
                break
            else:
                flag=0  # Similarly, this flag variable is local to the loop.
                break
        if(flag==1):
            print("not prime")
        else:
            print("prime")
            rev_no=0
            while num!=0:
                remainder=num%10
                rev_no=(rev_no*10)+remainder
                num//=10
            for i in range(2,rev_no):
                if(rev_no%i==0):
                    count=1  # This flag variable is local to the loop, it won't be accessible outside the loop.
                    break
                else:
                    count=0  # Similarly, this flag variable is local to the loop.
                    break
            if(count==1):
                print("not magical")
            else:
                print("magical")
    
num=int(input("enter no"))
p=prime()
p.cal(num)
