def Reverse_num(num):
    rnum = 0
    while int(num) > 0 :
        num = int(num)
        rnum = rnum + ((10**count_digits(num))*(num%10))
        #print(count_digits(num) , " and " , num%10 , "and Rnum : ",rnum)
        num/=10
    return str(rnum)

def count_digits(num):
    count = 1
    num = int(num)
    while int(num/10) > 0 :
        count+=1
        num/=10
    return (count-1)
if __name__=='__main__' :
    number = int(input("Enter a number to reverse : "))
    print(Reverse_num(number))