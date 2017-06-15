def find_missing(list1,list2):
    # return 0 if both are empty lists
    if len(list1) == 0 and len(list2) == 0:
        return 0
    #use bigger list to check for missing number
    if len(list1) > len(list2):
        for num in list1:
            if num not in list2:
                return num
    else:
        for num in list2:
            if num not in list1:
                return num
    # retun 0 if lists are equal
    return 0