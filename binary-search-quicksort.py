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


def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return sort(left) + middle + sort(right)

def main():
  import random
  arr = sort(random.sample(range(10,50000),5000))
  print(arr)
  key = int(input("Enter element to seach for"))
  result = binarysearch(arr,0,len(arr) - 1,key)
  if(result == -1):
    print("Element not found")
  else:
    print("Element found at ",result)

if __name__ == "__main__":
  main()




