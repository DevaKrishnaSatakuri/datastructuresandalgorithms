#CREATING A 1-D ARRAY
print("No of elements in the array",end="")
num=input()
arr=[]
print("Enter",num,"Element",end="")
num=int(num)
for i in range(num):
    element=input()
    arr.append(element)
print("The element in array are:")
for i in range (num):
    print(arr[i],end="")


#CREATING A 2-D ARRAY
r_num=int(input( "\nInput no. of rows: "))
c_num=int(input("Input no. of columns: "))
twod_arr=[[0 for col in range(c_num)]for row in range(r_num)]
for row in range(r_num):
    for col in range(r_num):
        twod_arr[row][col]=row*col
print(twod_arr)

