#Add part time employee & wage

def emp(n):
    
    for i in range(n):
        pemplist.append([input("enter name :"),int(input("enter wage :"))])
    print(pemplist)

pemplist=[]
emp(int(input("enter number of employees :")))