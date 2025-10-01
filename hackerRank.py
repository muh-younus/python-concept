
#List Comprehension
# x = int(input("Enter the x value"))
# y = int(input("Enter the y value"))
# z = int(input("Enter the z value"))
# n = int(input("Enter the n value"))
# result = []

# for i in range(x + 1):
#     print("i",i)
#     for j in range(y + 1):
#         print("j",j)
#         for k in range(z + 1):
#             print("k",k)
#             if i + j + k != n:
#                 result.append([i,j,k])
                
            

# print(result)

#Find runner score in the score sheet

# n = 5
# list =[]

# for score in range(2,8,1):
#     list.append(score)
# print(n)
# print(int(list))

# n = int(input())
    
# arr = list(map(int, input().split()))
# print("The array is:",arr)
# sorted= arr.sort()
# print("The sorted arry is: ",sorted)
# print(arr[arr.index(min(arr))])

# def cube(x):
#     return x * x
# cube(2)
    

# list1 = [3,4,5,6,5]
# newlist = list(map(cube,list1))
# print(newlist)

list = [2,3,4,5,6]

newList = tuple(map(lambda x: x**2,list))
print(list)
print(newList)

a = [1,2,3]
b = [4,5,6]

sum = tuple(map(lambda s,u: s+u,a,b))
print(sum)

