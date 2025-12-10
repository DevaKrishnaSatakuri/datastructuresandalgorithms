import array
# # #CREATING A 1-D ARRAY
# print("No of elements in the array",end="")
# num=int(input())
# arr=array.array("i",[])
# print("Enter", (num),"Element",end="")
# num=int(num)
# for i in range(num):
#     element=int(input())
#     arr.append(element)
# print("The elements in array are:")
# for i in range (num):
#     print(arr[i],end=" ")
#
#
# #CREATING A 2-D ARRAY
# r_num=int(input( "\nInput no. of rows: "))
# c_num=int(input("Input no. of columns: "))
# twod_arr=[[0 for col in range(c_num)]for row in range(r_num)]
# for row in range(r_num):
#     for col in range(r_num):
#         twod_arr[row][col]=row*col
# print(twod_arr)
#
# #DELETING AN ELEMENT IN AN ARRAY BY VALUE
# print(end="Size of the array : ")
# tot=int(input())
# arr=[]
# print(end="Enter" +str(tot)+ "elements : ")
# for i in range(tot):
#     arr.append(input())
# print("\nValue to be deleted : ")
# val=input()
# if val in arr:
#     arr.remove(val)
#     print("\nTHe new array is : ")
#     for i in range(tot-1):
#         print(end=arr[i]+" ")
# else:
#     print("\nElement doesn't exist in the array")
#
# #DELETING AN ELEMENT IN AN ARRAY BY INDEX
# print(end="Size of an array : ")
# tot=int(input())
# arr=[]
# print(end="Enter" +str(tot)+ "elements :")
# for i in range(tot):
#     arr.append(input())
# print("\nIndex to be deleted :")
# idx=int(input())
# if 0 <= idx < tot:
#     del arr[idx]
#     print("Modified array : ")
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
# else:
#     print("\nInvalid index")
#
#
# #SORTING OF AN ARRAY (ASCENDING)
# arr=array.array("i",[10,5,12,75,1])
# temp=0
#
# print("Elements of original array : ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i]>arr[j]):
#             temp=arr[i];
#             arr[i]=arr[j];
#             arr[j]=temp;
# print();
# print('Elements sorted in ascending order: ')
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")
#
# #SORTING OF AN ARRAY (DESCENDING)
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i]<arr[j]):
#             temp=arr[i];
#             arr[i]=arr[j];
#             arr[j]=temp
# print();
# print("Elements sorted in descending order : ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")
#
# #SORTING OF AN ARRAY WITHOUT ASSIGNING A TEMPORARY VARIABLE
# #APPROACH 1
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i]>arr[j]):
#             arr[i],arr[j]=arr[j],arr[i]
# print()
# print("Array in ascending order (approach 1) : ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")
#
# #APPROACH 2
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i]<arr[j]):
#             arr[i]=arr[i]+arr[j]
#             arr[j]=arr[i]-arr[j]
#             arr[i]=arr[i]-arr[j]
# print()
# print("Array in descending order:")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")

#SEARCHING THE INDEX OF AN ELEMENT
arr=array.array("u",["D", "S", "S", "A"])
print("\nThe created array is : ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print("\r")
print("The index of D : ", end="")
print(arr.index("D"))
print("\r")
print("The index of A : ", end="")
print(arr.index("A"))



