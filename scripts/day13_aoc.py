import re
from functools import cmp_to_key

def return_sum_of_indices_of_right_inputs(filename=None):
    try:
        result_list = []
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n\n')
        
        for i, input in enumerate(all_inputs):
            left = input.split('\n')[0]
            right = input.split('\n')[1]

            left = listify(left)
            right = listify(right)

            if test_right_vs_left(left, right) == True:
                result_list.append(i+1)

            
       
        print("done")
        return sum(result_list)
    except Exception as e:
        print("error in return_sum_of_indices_of_right_inputs fn", str(e))

def test_right_vs_left(left, right):
    '''Both the inputs should be type list
        Returns True if in right order, otherwise False or Equal
        Right order = True
        Wrong order = False'''
    try:
        # print('recursive call...')
        len_left = len(left)
        len_right = len(right)

        min_range = min(len_left, len_right)

        for item in range(min_range):
            if type(left[item]) == int and type(right[item]) == int:
                if left[item] > right[item]:
                    res = False
                elif left[item] < right[item]:
                    res = True
                else:
                    res = 'equal'
            elif type(left[item]) == list and type(right[item]) == int:
                res = test_right_vs_left(left[item], [right[item]])
            elif type(left[item]) == int and type(right[item]) == list:
                res = test_right_vs_left([left[item]], right[item])
            else:
                res = test_right_vs_left(left[item], right[item])
            
            if res in (False, True):
                return res

        if len_left > len_right:
            return False
        elif len_left < len_right:
            return True
        else :
            return 'equal'
    except Exception as e:
        print("error in test_right_vs_left fn", str(e))

def listify(list_string=None):
    '''Trying the stack way as regex way didnt work out'''
    try:
        list_string = list(re.findall(r'[,\]\[\s]|\d+', list_string))  # Grouping all of the numbers and characters.
        _stack = []
        _list = []
        new_list = None
        for item in list_string:
            if item == '[':
                new_list = []
                # _list.append(new_list)
                if _stack:
                    _stack[-1].append(new_list)
                _stack.append(new_list)
            elif item in (' ', ','):
                pass
            elif item == ']':
                _list = _stack[0][:]
                _stack.pop()
            else:
                _stack[-1].append(int(item))
        
        # print('done')
        return _list
    except Exception as e:
        print("error in listify fn", str(e))
        exit(-1)

def test_wrapper(left, right):
    res = test_right_vs_left(left, right)
    print(res)
    if res == 'equal':
        print('somebody testing equality folks')
        res = True
    return res

def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # if arr[j] > arr[j+1]:
            if not test_right_vs_left(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def return_product_of_placed_decoder_key(filename=None):
    try:
        result_list = []
        all_packets = []
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n\n')
        
        for i, input in enumerate(all_inputs):
            left = input.split('\n')[0]
            right = input.split('\n')[1]

            left = listify(left)
            right = listify(right)

            all_packets.append(left)
            all_packets.append(right)

        all_packets.extend([[[2]], [[6]]])
        # c = sorted(all_packets, key = cmp_to_key(test_wrapper) )  # Customr sorting didn't work for whatever reason.
        bubble_sort(all_packets)
        # d = all_packets.sort(key = cmp_to_key(test_right_vs_left))
        
        print("done")
        return (all_packets.index([[2]])+1)*(all_packets.index([[6]]) + 1)
    except Exception as e:
        print("error in return_product_of_placed_decoder_key fn", str(e))
if __name__=="__main__":
    input = './sample/sample13.txt'
    input = './input/advent_of_code_day13_input.txt'
    # input = './sample/sample13_2.txt'

    # result = return_sum_of_indices_of_right_inputs(filename=input)
    result = return_product_of_placed_decoder_key(filename=input)
    # a = [3, 2, -1, 5, 9, 2]
    # bubble_sort(a)
 
    # input_str = '[1,2,3,[4,5],6]'
    # # input_str = '[1, 2, 3, 6]'
    # input_str = '[1, 2, [10, [3, 4]], 5, [[11, 19], 12], 13, 14, [[[15]]]]'
    # input_str = '[1, 2, 3, 4, 6]'

    # new_list = listify(input_str)

    print(result)
    print('done')
