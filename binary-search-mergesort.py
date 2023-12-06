'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def merge_sort(arr):
    if(len(arr) > 1):
        
        # Division
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        #Merge Back
        i = j = k = 0
        while(i<len(left_arr) and j<len(right_arr)):
            if(left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
            k = k + 1

        while(i<len(left_arr)):
            
            arr[k] = left_arr[i]
            i =i + 1
            k = k + 1
        while(j<len(right_arr)):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1
    return arr    
    
def binarysearch(arr,low,high,key):
  while (low<=high):
    mid = (low + high)//2
    if (key == arr[mid]):
      return mid
    elif(key > arr[mid]):
      low = mid + 1
    else:
      high = mid - 1
  return -1



def main():
  import random
  arr = merge_sort(random.sample(range(10,50000),5000))
  print(arr)
  key = int(input("Enter element to seach for"))
  result = binarysearch(arr,0,len(arr) - 1,key)
  if(result == -1):
    print("Element not found")
  else:
    print("Element found at ",result)

if __name__ == "__main__":
  main()






