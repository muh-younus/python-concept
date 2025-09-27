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

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def average(self):
        total=0
        for val in self.mark:
            print(val)
            total += val
        
        print(total)
        print("The average is:",total/len(self.mark))


s1=student("Muhammad",[44,55,66])
s1.average()