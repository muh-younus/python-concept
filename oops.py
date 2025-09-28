# class student:
#     def __init__(self,name,mark1,mark2,mark3):
#          self.name = name
#          self.english = mark1
#          self.maths = mark2
#          self.science = mark3
#          self.ave = (mark1+mark2+mark3)/3
#     def average(self):
#             print("The average is: ",self.ave)
    

# s1 = student("Muhammad",56,43,32)
# print(s1.ave)
# print(s1.average())

# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def average(self):
#         total=0
#         for val in self.mark:
#             print(val)
#             total += val
        
#         print
#         print("The average is:",total/len(self.mark))


# s1=student("Muhammad",[44,55,66])
# s1.average()

#blance , account number

# class hbl_account:
#     def __init__(self,balance):
#         self.accountBalance = balance

#     def credit(self,amount):
#         self.accountBalance += amount
#         print("You credit amount is",amount)
#         print(self.total_balance())
#     def debit(self,amount):
#         self.accountBalance -= amount
#         print("You credit amount is",amount)
#         print(self.total_balance())
    
#     def total_balance(self):
#         print("Total balance is ",self.accountBalance)


# account = hbl_account(2000)
# account.credit(1000)
# account.debit(300)
# account.credit(2000)



# class book:
#     def __init__(self,name,year):
#         self.book_name=name
#         self.publish=year
#     def old(self,name):
#         self.old_name=name

    
# branch = book("Atomic Habit",2020)
# print(branch.book_name)
# del branch.book_name
# branch.auther = "James Clear"
# print(branch.auther)
# branch2 = book("Atomic Habit",2020)
# # print(branch2.auther)
# print(branch2.book_name)
# print(branch2.publish)

# print(branch2.old("jackma"))


#Inheritance

# 

class car:
    def __init__ (self ,model,year):
        self.model = model
        self.year = year
    @staticmethod
    def drive():
        print("The car is driving")

class suzuki(car):
    def __init__ (self,color,name,model,year):
        self.color = color
        self.name = name
        super().__init__(model,year)
        super().drive()

company = suzuki("red","swift","silion",2020)
print(company.model)
print(company.year)