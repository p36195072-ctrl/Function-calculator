try:
    def add(a , b):
      return (a + b)
    def sub(a , b):
        return (a - b)
    def multi(a , b):
        return(a * b)
    def divi(a , b):
        return (a / b)
    
    num1 = int(input("enter your number:"))
    num2 = int(input("enter your number:"))



    

    print("addition = ", add(num1 , num2))
    print("subtraction = ", sub (num1 , num2))
    print("division = ", divi (num1 , num2))
    print("multiplication = ", multi (num1 , num2))

except  ZeroDivisionError:
    print("can't be divided by 0")

except ValueError:
    print("Please enter valid numbers")


