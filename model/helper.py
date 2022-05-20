def findByBinarySearch(itemList, id):
  low = 0
  high = len(itemList) - 1
  mid = 0
  compareId = int(id)

  if len(itemList) == 0:
    return -1

  while low <= high:
      mid = (high + low) // 2
      if int(itemList[mid]['id']) < compareId:
          low = mid + 1
      elif int(itemList[mid]['id']) > compareId:
          high = mid - 1
      else:
          return mid

  return -1