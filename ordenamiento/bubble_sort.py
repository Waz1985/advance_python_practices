my_list = [1, 10, 4, 3, 8, 2, 25, 7]

def bubble_sort(list_to_order):
    list_len = len(list_to_order) -1

    for it_num in range(list_len):
        swapped = False

        for i in range(list_len - it_num):
            current = i
            next = i + 1
            print(list_to_order[current], list_to_order[next])

            if list_to_order[current] > list_to_order[next]:
                list_to_order[current], list_to_order[next] = list_to_order[next], list_to_order[current]

                swapped = True

            print(f"List: {list_to_order}")  
            
        if not swapped:
            break
            
        print(f"iterations:{list_len - it_num}")
    print(f"Ordered list: {list_to_order}")


def inverted_bubble_sort(list_to_order):
    list_len = len(list_to_order)

    for it_num in range(list_len):
        swapped = False

        for i in range(list_len -1, it_num, - 1):
            current = i
            next = i - 1
            print(list_to_order[current], list_to_order[next])
            
            if list_to_order[current] < list_to_order[next]:
                list_to_order[current], list_to_order[next] = (list_to_order[next], list_to_order[current])
                swapped = True
            
            print(f"List: {list_to_order}")  
        
        if not swapped:
            break
            
        print(f"iterations:{list_len - it_num}")
    print(f"Ordered list: {list_to_order}")



inverted_bubble_sort(my_list)