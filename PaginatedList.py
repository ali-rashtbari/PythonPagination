
# sample lists ---
def Items1(start:int, end:int):
    my_list = [num for num in range(1, 100)]
    return my_list[start:end]

def Items2(start:int, end:int):
    my_list = [num for num in range(1, 100)]
    return my_list[start:end]

def Items3(start:int, end:int):
    my_list = [num for num in range(1, 100)]
    return my_list[start:end]

def Items4(start:int, end:int):
    my_list = [num for num in range(1, 100)]
    return my_list[start:end]


# defs store ---
defs_name_dict = {
    "Items1" : Items1,
    "Items2" : Items2,
    "Items3" : Items3,
    "Items4" : Items4,
}

# pagination list as paginated lists ---
for key, value in defs_name_dict.items():
    counter = 20  # page size ---
    start = 0
    while(True):
        end = start + counter
        result = value(start=start, end=end)
        if len(result) <= 0:
            break
        print(result)
        start = end


