a="bob"
b="john"
c="tom"
bob_amount=input("what is bob money?")
print(bob_amount)
john_amount=input("what is john money?")
print(john_amount)
tom_amount=input("what is john tom?")
print(tom_amount)
if(bob_amount==tom_amount)&(tom_amount==john_amount):
 print("All of them have the same amount of money")
elif(bob_amount>john_amount)& (john_amount>tom_amount):
    print(a," is richer than", b,"while",b,"is richer than",c)
elif(bob_amount>tom_amount)& (tom_amount==john_amount):
    print(a," is richer than", c,"while",c,"is equal to",b)
 elif (john_amount>tom_amount)& (tom_amount>bob_amount):
    print(b," is richer than", c,"while",c,"is richer than",a)
elif(john_amount>tom_amount)& (tom_amount==bob_amount):
    print(b," is richer than", c,"while",c,"is equal to",c)
print("my name is ",a)
  

elif(tom_amount>bob_amount)& (bob_amount>john_amount):
    print(c," is richer than", a,"while",a,"is richer than",b)
elif(tom_amount>bob_amount)& (bob_amount==john_amount):
     print(c," is richer than", a,"while",a,"is equal to",b)

else:
    print("This is Not Possible")


monthly_income=6500
monthly_rent=3000
rem = monthly_income - monthly_rent



 budget=(70/100)*rem
 print("You budget should be:kshs.",budget)



 savings=rem-budget
print("Expected Monthly savings :kshs.",savings)

# year_savings=savings*12
# print("Expected Yearly Savings:kshs.",year_savings)


# x=10000
# while x>100 :
#  print(x)
# x-=1
