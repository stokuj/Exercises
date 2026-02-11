# Write your solution here

def list_sum(list1 : list, list2 : list) -> list:
    
    for n in range(len(list1)):
        list1[n] = list1[n] + list2[n]
        
    return list1

#print(list_sum([1,2,3],[2,4,6]))