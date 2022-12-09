from functools import reduce
import re

def find_externally_visible_tree_count(filename=None):
    try:
        tree_ht_list = []

        with open(filename, 'r') as f:
            lines = f.read().strip()
        
        for line in lines.split('\n'):
            tree_ht_list.append(list(map(int, re.findall(r'\d+?', line.strip()))))

        width = len(tree_ht_list[0])
        length = len(tree_ht_list)

        visible_tree_count = 2 * (width + length) - 4

        for i in range(1, length-1):
            for j in range(1, width-1):
                tree_height = tree_ht_list[i][j]
                # print(f'[{i}][{j}]--{tree_ht_list[i][j]}')

                row_left = tree_ht_list[i][:j]
                row_right = tree_ht_list[i][j+1:]

                column_height = []
                for k in range(length): column_height.append(tree_ht_list[k][j])
                column_height_up = column_height[:i]
                column_height_down = column_height[i+1:]

                large_tree_bool_row_left = list(map(lambda x:x >= tree_height, row_left))
                large_tree_bool_row_right = list(map(lambda x:x >= tree_height, row_right))

                not_visible_row_left = reduce(lambda x,y: x or y, large_tree_bool_row_left, False)
                not_visible_row_right = reduce(lambda x,y: x or y, large_tree_bool_row_right, False)
                
                large_tree_bool_col_up = list(map(lambda x:x >= tree_height, column_height_up))
                large_tree_bool_col_down = list(map(lambda x:x >= tree_height, column_height_down))

                not_visible_column_up = reduce(lambda x,y: x or y, large_tree_bool_col_up, False)
                not_visible_column_down = reduce(lambda x,y: x or y, large_tree_bool_col_down, False)

                if not (not_visible_row_left and not_visible_row_right and not_visible_column_up and not_visible_column_down):
                    visible_tree_count += 1
                    print(f'{j}....{i}---{tree_ht_list[j][i]}')
                # print('a')
        print('done')
        return visible_tree_count
        print('yo')

    except Exception as e:
        print("error in find_externally_visible_tree_count fn" ,str(e))
def find_externally_visible_tree_count(filename=None):
    try:
        tree_ht_list = []

        with open(filename, 'r') as f:
            lines = f.read().strip()
        
        for line in lines.split('\n'):
            tree_ht_list.append(list(map(int, re.findall(r'\d+?', line.strip()))))

        width = len(tree_ht_list[0])
        length = len(tree_ht_list)

        visible_tree_count = 2 * (width + length) - 4

        for i in range(1, length-1):
            for j in range(1, width-1):
                tree_height = tree_ht_list[i][j]
                # print(f'[{i}][{j}]--{tree_ht_list[i][j]}')

                row_left = tree_ht_list[i][:j]
                row_right = tree_ht_list[i][j+1:]

                column_height = []
                for k in range(length): column_height.append(tree_ht_list[k][j])
                column_height_up = column_height[:i]
                column_height_down = column_height[i+1:]

                large_tree_bool_row_left = list(map(lambda x:x >= tree_height, row_left))
                large_tree_bool_row_right = list(map(lambda x:x >= tree_height, row_right))

                not_visible_row_left = reduce(lambda x,y: x or y, large_tree_bool_row_left, False)
                not_visible_row_right = reduce(lambda x,y: x or y, large_tree_bool_row_right, False)
                
                large_tree_bool_col_up = list(map(lambda x:x >= tree_height, column_height_up))
                large_tree_bool_col_down = list(map(lambda x:x >= tree_height, column_height_down))

                not_visible_column_up = reduce(lambda x,y: x or y, large_tree_bool_col_up, False)
                not_visible_column_down = reduce(lambda x,y: x or y, large_tree_bool_col_down, False)

                if not (not_visible_row_left and not_visible_row_right and not_visible_column_up and not_visible_column_down):
                    visible_tree_count += 1
                    print(f'{j}....{i}---{tree_ht_list[j][i]}')
                # print('a')
        print('done')
        return visible_tree_count
        print('yo')

    except Exception as e:
        print("error in find_externally_visible_tree_count fn" ,str(e))
def find_maximum_scenic_score(filename=None):
    try:
        tree_ht_list = []
        max_scenic_score = 0

        with open(filename, 'r') as f:
            lines = f.read().strip()
        
        for line in lines.split('\n'):
            tree_ht_list.append(list(map(int, re.findall(r'\d+?', line.strip()))))

        width = len(tree_ht_list[0])
        length = len(tree_ht_list)

        visible_tree_count = 2 * (width + length) - 4

        for i in range(1, length-1):
            for j in range(1, width-1):
                tree_height = tree_ht_list[i][j]
                # print(f'[{i}][{j}]--{tree_ht_list[i][j]}')

                row_left = tree_ht_list[i][:j]
                row_right = tree_ht_list[i][j+1:]

                column_height = []
                for k in range(length): column_height.append(tree_ht_list[k][j])
                column_height_up = column_height[:i]
                column_height_down = column_height[i+1:]
                

                count_row_right = 0
                for k in row_right:
                    count_row_right += 1
                    if (k >= tree_height):
                        break
                count_row_left = 0
                for k in row_left[::-1]:
                    count_row_left += 1
                    if (k >= tree_height):
                        break
                count_col_down = 0
                for k in column_height_down:
                    count_col_down += 1
                    if (k >= tree_height):
                        break
                count_col_up = 0
                for k in column_height_up[::-1]:
                    count_col_up += 1
                    if (k >= tree_height):
                        break
                
                scenic_score = count_row_left * count_row_right * count_col_up * count_col_down

                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score

                print('a')
        print('done')
        return max_scenic_score
        print('yo')

    except Exception as e:
        print("error in find_externally_visible_tree_count fn" ,str(e))

if __name__=="__main__":
    input = './sample/sample8.txt'
    input = './input/advent_of_code_day8_input.txt'

    # result = find_externally_visible_tree_count(filename=input)
    result = find_maximum_scenic_score(filename=input)

    print(result)