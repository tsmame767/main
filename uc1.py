#check whether the employee is present or not
def presence():
    user=int(input("enter 1 for present 0 for absent: "))
    if user==1:
        return "present"

    else:
        return "absent"
    
presence()