import re
import pickle
from functools import reduce

def gcd(a, b):
    ''' Only for Integers and doesnot handles zero as input case.'''
    try:
        divisor = min(a, b)
        dividend = max(a, b)
        
        while(True):
            rem = dividend % divisor
            if rem == 0:
                return divisor
            elif rem == 1:
                return 1
            dividend = divisor
            divisor = rem
    except Exception as e:
        print("error in gcd fn", str(e))

def lcm(*args):
    try:
        result = reduce(lambda a,b: a*b//gcd(a,b), *args, 1)
        return result
    except Exception as e:
        print("error in lcm fn", str(e))
def return_count_of_monkey_shinanigans(filename=None):
    try:
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n\n')
        monkeys_item_dict = {}
        inspect_dict = {}
        for input in all_inputs:
                monkey_process = input.strip().split('\n')
                monkey_id = int(monkey_process[0].strip().split(':')[0].split(' ')[1])
                monkey_items = list(map(int, monkey_process[1].split(':')[1].strip().split(',')))
                operator, number = monkey_process[2].strip().split('=')[1].strip().split(' ')[1:]
                divisor = int(monkey_process[3].strip().split(' ')[-1])
                true_throw = int(monkey_process[4].strip().split()[-1])
                false_throw = int(monkey_process[5].strip().split()[-1])
                monkeys_item_dict[monkey_id] = {'monkey_items': monkey_items,
                                                'operator': operator,
                                                'number': number,
                                                'divisor': divisor,
                                                'true_throw': true_throw,
                                                'false_throw': false_throw
                                                }
                # print(f'{monkey_id}--{monkey_items}--{operator}--{number}--{divisor}--{true_throw}--{false_throw}')

        for i in range(20):
            print(f'---{i}--done')
            for monkey_id, actions in monkeys_item_dict.items():
                # for item in actions['monkey_items']:
                while(actions['monkey_items']):
                    item = actions['monkey_items'].pop(0)
                    if actions['number'] == 'old':
                            number = item
                    else:
                        number = int(actions['number'])
                    
                    if actions['operator'] == '*':
                        worry_level = item * number
                    elif actions['operator'] == '+':
                        worry_level = item + number
                    
                    # worry-level after monkey gets bored, worry-level gets divided by 3 (floor)
                    worry_level = worry_level // 3

                    if worry_level % actions['divisor'] == 0:
                        monkeys_item_dict[actions['true_throw']]['monkey_items'].append(worry_level)
                    else:
                        monkeys_item_dict[actions['false_throw']]['monkey_items'].append(worry_level)
                    
                    if monkey_id in inspect_dict:
                        inspect_dict[monkey_id] += 1
                    else:
                        inspect_dict[monkey_id] = 1
        
        print('done')
        most_activities = sorted(list(inspect_dict.values()))[-2:]

        return most_activities[0] * most_activities[1]
    except Exception as e:
        print("error in return_count_of_money_shinanigans fn", str(e))

def return_count_of_monkey_ispection_unmanageable_worry(filename=None):
    try:
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n\n')
        monkeys_item_dict = {}
        inspect_dict = {}
        for input in all_inputs:
                monkey_process = input.strip().split('\n')
                monkey_id = int(monkey_process[0].strip().split(':')[0].split(' ')[1])
                monkey_items = list(map(int, monkey_process[1].split(':')[1].strip().split(',')))
                operator, number = monkey_process[2].strip().split('=')[1].strip().split(' ')[1:]
                divisor = int(monkey_process[3].strip().split(' ')[-1])
                true_throw = int(monkey_process[4].strip().split()[-1])
                false_throw = int(monkey_process[5].strip().split()[-1])
                monkeys_item_dict[monkey_id] = {'monkey_items': monkey_items,
                                                'operator': operator,
                                                'number': number,
                                                'divisor': divisor,
                                                'true_throw': true_throw,
                                                'false_throw': false_throw
                                                }
        all_div_test_numbers = [x['divisor'] for x in monkeys_item_dict.values()]
        lcm_all_divisors = lcm(all_div_test_numbers)

        for i in range(10000):
            for monkey_id, actions in monkeys_item_dict.items():
                while(actions['monkey_items']):
                    item = actions['monkey_items'].pop(0)
                    if actions['number'] == 'old':
                            number = item
                    else:
                        number = int(actions['number'])
                    
                    if actions['operator'] == '*':
                        worry_level = item * number
                    elif actions['operator'] == '+':
                        worry_level = item + number
                    
                    # worry-level no longer gets divided by 3 (floor), second part of the puzzle.
                    # worry_level = worry_level // 3

                    if worry_level % actions['divisor'] == 0:
                        monkeys_item_dict[actions['true_throw']]['monkey_items'].append(worry_level % lcm_all_divisors)
                    else:
                        monkeys_item_dict[actions['false_throw']]['monkey_items'].append(worry_level % lcm_all_divisors)
                    
                    if monkey_id in inspect_dict:
                        inspect_dict[monkey_id] += 1
                    else:
                        inspect_dict[monkey_id] = 1

        most_activities = sorted(list(inspect_dict.values()))[-2:]
        return most_activities[0] * most_activities[1]
    except Exception as e:
        print("error in return_count_of_monkey_inspectios_unmanageable_worry fn", str(e))
if __name__=="__main__":
    input = "./sample/sample11.txt"
    input = "./input/advent_of_code_day11_input.txt"

    # result = return_count_of_monkey_shinanigans(filename=input)
    result = return_count_of_monkey_ispection_unmanageable_worry(filename=input)

    print(result)