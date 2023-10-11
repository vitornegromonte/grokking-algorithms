def minimum_search(list):
    low = list[0]
    lower_index = 0
    
    for i in range(1, len(list)):
        if list[i] < low:
            low = list[i]
            lower_index = i
            
    return lower_index

def selection_search(list):
    newArray = []
    for x in range(len(list)):
        low = minimum_search(list)
        newArray.append(list.pop(low))
    return newArray
        
print(selection_search([5,3,6,2,10]))