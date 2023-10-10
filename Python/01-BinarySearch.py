def binary_search(list: list, item: int):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = int((low + high) / 2)
    guess = list[mid]

    if guess == item:
      return mid
    
    elif guess > item:
      high = mid - 1
    
    else:
      low = mid + 1
  
  return None

if __name__ == '__main__':
  sample_list = [1,3,5,7,9]

  print(binary_search(sample_list, 3)) # => 1 [index 1 == 3]
  print(binary_search(sample_list, -1))# => None [there's none -1 value in the sample list]