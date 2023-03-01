import cmath as cm


def quadratic_eqn ():
    a= int(input("Enter the non zero value of a : "))
    b= int(input("Enter the value of b : "))
    c= int(input("Enter the value of c : "))
    part1 = (b**2)-(4*a*c)
    root1 = (-b + cm.sqrt(part1))/(2*a) 
    root2 = (-b - cm.sqrt(part1))/(2*a) 
    print(root1)
    print(root2)


quadratic_eqn()
