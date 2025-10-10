# Nested List
# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
# solution

# if __name__ == '__main__':
#   studentRecord = []
#   grade = []
#   for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         studentRecord.append([name,score])
#         grade.append(score)
# grade = sorted(set(grade))
# m = grade[1]
# name = []
# for val in studentRecord:
#     if m == val[1]:
#         name.append(val[0])
# for m in name:
#     print(m)


# dict1 ={

#     "ALi": [12,3,12,33],
#     "jackma":[12,3,12,33],
#     "Arif":[12,3,12,33],

# }

# queryName = "Arif"
# print(len(dict1[queryName]))

# sum = 0


# for i in dict1[queryName]:
#     num = int(i)
#     sum += num

# average = sum/len(dict1[queryName])
# # print(average)
# print(f"{average:.2f}")  # Output: 56.00

# lst = []
# command =[
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# ]
# N = input()
# lst = []
# for j in range(int(N)):
#     command = input().split() #insert 0 5
#     if(command[0] == "insert"):
#         lst.insert(int(command[1]),int(command[2]))
        
#     elif command[0] == "print":
#         print(lst)
#     elif command[0] == "remove":
#         list.remove(int(command[1]))
#     elif command[0] == "append":
#         lst.append(int(command[1]))
#     elif command[0] == "sort":
#         lst.sort()
#     elif command[0] == "print":
#         print(lst)
#     elif command[0] == "pop":
#         lst.pop()
#     elif command[0] == "reverse":
#         lst.reverse()
#     elif command[0] == "print":
#         print(lst)

# if __name__ == '__main__':
#     # Step 1: take number of elements
#     n = int(input("Enter number of elements: "))

#     # Step 2: take list of integers
#     integer_list = map(int, input("Enter numbers separated by space: ").split())

#     # Step 3: convert to tuple
#     t = tuple(integer_list)

#     # Step 4: print tuple and its hash value
#     print("Tuple:", t)
#     print("Hash value:", hash(t))

# a = "I am Muhammad Younus"
# split_a = a.split()
# print(type(split_a))
# split_a = "-".join(split_a)
# print(split_a)
# print(type(split_a))
def count_substring(string, sub_string):
    letter = string
    
    
    return print(letter.count(sub_string)) 
 
if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)
