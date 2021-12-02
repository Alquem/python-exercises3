chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    list1_2 = []
    for i in list1:
        list1_2.append(i)
    for i in list2:
        list1_2.append(i)
    
    return list1_2
print(merge_list(chunk_one, chunk_two))
