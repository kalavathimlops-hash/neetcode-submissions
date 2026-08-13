from typing import List

def remove_elements(arr: List[int], element: int) -> List[int]:
    arr_clone=arr.copy()
    arr_clone.remove(element)
    return arr_clone

arr=[1,3,5,7,9]

print(remove_elements(arr,3))
print(arr)
print(remove_elements(arr,9))
print(arr)
print(remove_elements(arr,1))
print(arr)