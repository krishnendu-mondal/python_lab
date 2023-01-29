l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

def are_lists_equal(list1, list2):
    if len(list1) == len(list2):
        if(list1 == list2):
            return True
        else:
            return False
    else:
        return False
print(are_lists_equal(l1, l2))