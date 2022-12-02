

def find_highest_calorie_of_elf(filename=None):
    try:
        highest_cal = 0
        current_calorie = 0
        current_value = 0
        with open(filename, 'r') as f:
            try:
                while(True):    
                    line = next(f).strip()
                    if line !='':
                        current_calorie += int(line)
                    else:
                        if current_calorie > highest_cal:
                            highest_cal = current_calorie
                        current_calorie = 0
                    # print(line.strip())
        
            except StopIteration:
                print('EOF reached')
        
        return highest_cal
    except Exception as e:
        print("error in find_highest_calorie_elf fn", str(e))
        return 0
def find_total_of_top_three_calories(filename=None):
    try:
        top_calorie_list = [0,0,0]
        current_calorie = 0
        current_value = 0
        with open(filename, 'r') as f:
            try:
                while(True):    
                    line = next(f).strip()
                    if line !='':
                        current_calorie += int(line)
                    else:
                        top_calorie_list.append(current_calorie)
                        top_calorie_list.sort()
                        top_calorie_list.pop(0)
                        current_calorie = 0
                    # print(line.strip())
            except StopIteration:
                print('EOF reached')
                if current_calorie > 0:
                    top_calorie_list.append(current_calorie)
                    top_calorie_list.sort()
                    top_calorie_list.pop(0)
                    current_calorie = 0
        
        return sum(top_calorie_list)
    except Exception as e:
        print("error in find_highest_calorie_elf fn", str(e))
        return 0

if __name__=="__main__":
    input = 'advent_of_code_day1_input.txt'
    # input = 'sample.txt'
    # highest_cal = find_highest_calorie_of_elf(filename=input)
    total_of_top_three = find_total_of_top_three_calories(filename=input)
    print(total_of_top_three)