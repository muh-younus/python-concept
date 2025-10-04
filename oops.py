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

# blance , account number

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


# Inheritance





# n = 3
    
# if(n > 0 or n < 6):
#     if(n % 2 ==0):
#         print("Not Weird",n)
#     else:
#         print("Weird",n)  
    
# n=24
# if (n > 6 and n < 21):
#     if(n % 2 == 0):
#         print("Weird",n)
#     else:
#          print("Not Weird",n) 
        
studentRecord = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akriti", 41],
    ["Harsh", 39]
] 

# grade = [37.21,37.21,37.2,41,39]
# grade = sorted(set(grade))
# m = grade[1]
# print("the student record is ", studentRecord)
# print("the grade is ",grade) 
# name = []

# for val in studentRecord:
    
#     if(m == val[1]):
#         print("val 1 is",val[1])
#         print("val[0] is",val[0])
#         name.append(val[0])
# print(name)

# # for _ in range(int(input())):
# #     name = input()
# #     score = float(input())
# #     studentRecord.append([name, score])
    
# print(studentRecord)
# sortedRecord = sorted(studentRecord, key=lambda x: x[1])
# print(sortedRecord)

n = int(input())
result = []
grade = []

for i in range(n):
    name = input()
    mark = float(input())
    result.append([name,mark])
    grade.append(mark)

print(result)
print(grade)
grade = sorted(set(grade)) 
m = grade[1]
name = []

for val in result:
    if(m == val[1]):
        name.append(val[0])



for i in name:
    print(i)