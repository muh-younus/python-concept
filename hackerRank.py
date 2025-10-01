x = int(input("Enter the x value"))
y = int(input("Enter the y value"))
z = int(input("Enter the z value"))
n = int(input("Enter the n value"))
result = []

for i in range(x + 1):
    print("i",i)
    for j in range(y + 1):
        print("j",j)
        for k in range(z + 1):
            print("k",k)
            if i + j + k != n:
                result.append([i,j,k])
                
            

print(result)


