# arr =[3,10,5,1,4]
# min = 1
# max = 0
# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]
#     if arr[i] > max:
#         max = arr[i]
#     i+=1
# print(min,max)
# ------------------------------------------------------------------
# min = arr[0]
# max = arr[0]
# i=0
# ------------------------------------------------------------------
# while i < len(arr):
#     if arr[i] < min:
#         min = arr[i]
#     if arr[i] > max:
#         max = arr[i]
#     i+=1
# print(max,",",min)

#1.Contains Duplicates (arrays) -------> using sets
arr= [1,2,3,4,1,2]

sett = set(arr)
print(sett)

if len(set(arr)) == len(arr):
    print(False)
else:
    print(True)

#2. Missing Number (array) --------> 

arr= [1,0,3]

print(len(arr))

print(len(arr)+1)

print((sum(range(len(arr)+1))) - sum(arr))
