from typing import List

def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    output=[]
    for i in nested_arr:
        max_in_arr=i[0]
        for i1 in i:
          max_in_arr=max(max_in_arr,i1)
        output.append(max_in_arr)
    return output    


print(find_max_in_each_list(([1,2],[3,4,2])))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))           
