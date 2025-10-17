# list = ["Haleem", 12, "english", 3.5, True]
# print(list)
# print(type(list))
# print(len(list))
# list[0]="zia ul haq"
# print(list)
# subList = list[1:3]
# print(subList)
# list = [12,45,56,43,34]
# list.append(100)

# list.insert(2,200)
# print(list)

# # Practise Questions

# movie1 = input("Enter your favourite movie name")
# movie2 = input("Enter your second favourite movie name")
# movie3 = input("Enter your third favourite movie name")

# list =[]
# list.append(movie1)
# list.append(movie2)     
# list.append(movie3) 
# print(list)

# list = ["kick", "nuen", "level" "Zee"]
# str= list[0]

# if(str[0] == str[len(str)-1]):
#     print("The string is palindrome")
# else:
#     print("The string is not palindrome")
# mydict = {
#     "name": "Muhammad Younus",
#     "age" : 34,
#     "Class": "SE",
#     "roll": 10
# }

# print(list(mydict))          # ['name', 'age', 'Class', 'roll']
# print(list(mydict.values())) # ['Muhammad Younus', 34, 'SE', 10]
# print(list(mydict.items()))  # [('name', 'Muhammad Younus'), ('age', 34), ('Class', 'SE'), ('roll', 10)]
# new_dict = {

#     "subject": {
#         "name": "python",
#         "code": 101
#     },
#     "Year": 2023
# }
# mydict.update(new_dict)
# print(mydict)
# mydict["location"] = "Karachi"
# print(mydict)
# print(list(mydict))
# print(mydict["subject"]["code"])  # python
# print(mydict.get("age"))

# dict1 = {
#     "table": ["a pieace of furniture","I am made by wood"],
#     "cat": "a small animal",


# }
# print(dict1)
# print(len(dict1))
# print(dict1.items())
# print(dict1.values())

# new_dict1 = {

#     "pen": "a pieace of stationery",
#     "laptop": "a pieace of computer"
# }  # dict_items([('table', 'a pieace of furniture'), ('cat', 'a small animal')])


# list = {"python", "java",  "c++","python", "javascript", "java", "python","java", "c++","c"}
# print(list)

# print("we need", len(list), " classrooms for the students",)

# mark_dict = {


# }

# mark_dict["sub1"] = int(input("Enter your marks for " ))
# mark_dict["sub2"] = int(input("Enter your marks for " ))
# mark_dict["sub3"] = int(input("Enter your marks for " ))
# print(mark_dict)
# set = {9, "9.0"}
# print(set)  # {9, 10}

# set = {

#     ("int",9),
#     ("float",9.0)
# }

# print(len(set))  # 2
# print(set)

# f = open('word.txt',"r")
# data = f.read()
# newData=data.replace("everyone","anyone")
# print(data)
# print(newData)

# w = open("word.txt","w")
# data = w.write(newData)
# print(data)
if __name__ == '__main__':
    s = input()


print(any(ch.isalnum() for ch in s))   # Alphanumeric
print(any(ch.isalpha() for ch in s))   # Alphabet
print(any(ch.isdigit() for ch in s))   # Digit
print(any(ch.islower() for ch in s))   # Lowercase
print(any(ch.isupper() for ch in s))