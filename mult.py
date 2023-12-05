def mult_lists(l1,l2):
    updated_list = []
    for i in l1:
        num = i
        for j in l2:
            num = num * j
        updated_list.append(num)
    return updated_list

mult_lists([1,2,3,4,5],[1,2,3,4,5])