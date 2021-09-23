# #a=30
# #b=50
# #c=a+b
# #print("the sum a plus b",c)
# #d=a-b
# #print("the difference of a - b",d)
# #e=a/b
# #print("the division of a divided b",e)
# #f=a*b
# #print("the product a multiplied b",f)
# #g=a%b
# #print("the modulus a and b",g)
#
#
# amount = int(input("how many people")) # sets amount to user input
#
#
#
# people = {} # creates an empty dictionary2
#
#
#
# average = 0 # sets average
#
#
#
# # for all numbers in the range of zero to amount
#
# for x in range(0, amount):
#
#               name = input("what is the persons name? ") # set persons name to input
#
#               people[name] = int(input("age?")) # creates a dictionary key of person name, with value age, from input
#
#
#
# # for all values in all values in people dictionary
#
# for ages in people.values():
#
#               average += ages # add age of each person to average
#
#
#
# print("the average age of all the people is ", average / amount) # divides average by amount of people to get real average
#
#
#
# print("the oldest person is ", max(people.values())) # min function gets smallest number in values
#
#
#
# print("the youngest person is ", min(people.values())) # max function gets largest number in values
#
#
#
# print() # print blank line
#
#
#
# print("all the people are: ")
#
#
#
# print(people) # prints entire dictionary
#
#
