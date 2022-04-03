flat_list = []




def ModifyList(_2d_list):

    for element in _2d_list:
        if type(element) is list:
            ModifyList(element)
        else:
            flat_list.append(element)
    return flat_list


nested_list = [ [1, 'a', ['cat'], 2], [[[3]], 'dog'],4, 5]
print(ModifyList(nested_list))
