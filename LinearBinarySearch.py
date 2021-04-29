#7. Searching: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[]. Do it using linear and binary search techniques.

def linear_search(arr,x):
    arr.sort()
    print("Linear Search:")
    print(f"Sorted Array: {arr}")
    temp=False
    
    for i in range(len(arr)):
        if x==arr[i]:
            print(f"X={x} found in the array at index {i}" )
            temp=True
            break
    
    if temp==False:
        print(f"X={x} not found in the array")
            
    
def binary_search(arr,x):
    arr.sort()
    print("Binary Search:")
    print(f"Sorted Array: {arr}")
    temp=False
    low=0
    high=int(len(arr))
    mid=int((low+high)/2)
    
    while high>mid:
        if arr[mid]==x:
            temp=True
            index=mid
            break
        elif arr[mid] < x:
            low=mid+1
        elif arr[mid] > x:
            high = mid-1
        mid=int((low+high)/2)
        
    if temp==True:
        print(f"X={x} found in the array at index {index}")
    elif temp==False:
        print(f"X={x} not found in the array")
    
arr=[0,1,2,3,4]
x=10
linear_search(arr,x)
binary_search(arr,x)
