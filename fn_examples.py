
class BasicPrograms:
     
    def this_function(self):
        print("This is a function")


    def my_percentage(self,obtained_marks,total_marks):
        thispercentage= (obtained_marks/total_marks)*100
        return thispercentage

    # percentage = my_percentage(450,635)
    # print(percentage)

    def check_even_odd(self,number_to_check):

        if(number_to_check %2==0):
            print(f"The given number {number_to_check} is Even")
        else:
            print(f"The given number {number_to_check} is Odd")


    # check_even_odd (100)
    # check_even_odd (99)

    def check_age_groups (self,age):

        if(age < 18 ):
            print("He or She is a Child")
        elif (age  > 18  and age <= 55 ):
            print ("He or She is an Adult")
        elif (age  > 55):
            print ("He or She is a Senior citizen")

    #check_age_groups(40)

    def temperatures_conversion(self):
        temp1= int(input("Enter the temperature to convert from F to C :  "))
        temp2= int(input("Enter the temperature to convert from C to F :  "))

        formula1= (temp1 - 32) * (5/9)
        formula2= temp2 *(9/5) + 32

        print ("Conversion from F to C :",formula1,"C")
        print ("Conversion from C to F :",formula2,"F")

    #temperatures_conversion()


    def vowel_or_not(self):
        sha= input("Enter the alpha : ")
        if (sha == 'a' or sha =='e' or sha =='i' or sha =='o' or sha =='u'):
            print ("It is a Vowel")
        else:
            print ("It is a consonent")

    #vowel_or_not()

    def reverse_word(self):
        word= input("Enter thw word : ")
        print (word[::-1])

    #reverse_word()


    def number_multi_by_5 (self):
        number= int(input("Enter the number : "))
        if (number % 5 == 0):
            print ("Hello")
        else:
            print ("Byee")


    def great_and_sallest_of_3_num(self):
        num1= int(input("Enter the number : "))
        num2= int(input("Enter the number : "))
        num3= int(input("Enter the number : "))

        if (num1 > num2 and num1> num3):
            print (num1, "is greatest number")
        elif (num2 > num1 and num2> num3):
            print (num2, "is greatest number")
        elif (num3 > num1 and num3> num2):
            print (num3, "is greatest number")
        else:
            print("numbers are equale")

        if (num1 < num2 and num1< num3):
            print (num1, "is smallest number")
        elif (num2 < num1 and num2< num3):
            print (num2, "is smallest number")
        elif (num3 < num1 and num3< num2):
            print (num3, "is smallest number")
        else:
            print("numbers are equale")
        

    def number_in_letters(self):
        num= int(input("Enter the number : "))
        if (num == 1):
                print ("One")
        elif (num == 2):
                print ("Two")
        elif (num == 3):
                print ("Three")
        elif (num == 4):
                print ("Four")
        elif (num == 5):
                print ("Five")
        elif (num == 6):
                print ("Six")
        elif (num == 7):
                print ("Seven")
        elif (num == 8):
                print ("Eight")
        elif (num == 9):
                print ("Nine")
        elif (num == 10):
                print ("Ten")
        else:
            print("Enter the number between 1 to 10")




if __name__ == "__main__":
    #Object of the class
    bp = BasicPrograms()
    
    print("Please select the number from below ")
    print("1.Calculate Percentage \n2.Convert Temp to and from F, C\n3.Even Odd\n4.Check age group\n5.Vowel or not\n6.Reverse word\n7.Print Hello if multi by 5 else Bye\n8.Greatest & smallest of 3 numbers\n9.Numbers in letters 1 to 10")
    opt = int(input())

    if (opt == 1):
        ob_marks = int(input("Enter the Obtained marks : "))
        total = int(input("Enter the total marks : "))
        percentage = bp.my_percentage(ob_marks,total)
        print(f"The percentage gained by you is {percentage}%")
    elif(opt == 2):
        bp.temperatures_conversion()
    elif (opt == 3):
        num = int(input("Enter the number to check Even Odd : "))         
        bp.check_even_odd(num)
    elif (opt == 4):
         age = int(input("Enter the age to check : "))
         bp.check_age_groups(age)
    elif (opt == 5):
         bp.vowel_or_not()
    elif (opt == 6):
         bp.reverse_word()
    elif (opt == 7):
         bp.number_multi_by_5()
    elif (opt == 8):
         bp.great_and_sallest_of_3_num()
    elif (opt == 9):
         bp.number_in_letters()
        