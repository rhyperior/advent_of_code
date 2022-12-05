import re

class Stack:
    def __init__(self, starting_creates=None):
        self._stack = []

        if starting_creates is not None:
            for crate in enumerate(starting_creates):
                self.push(crate[1])
    
    def push(self, crate):
        if type(crate) == list:
            self._stack.extend(crate)
        else:
            self._stack.append(crate)
    def pop(self, num=None):
        try:
            if not num:
                return self._stack.pop()
            else:
                popped_list = self._stack[-1*num:]
                del self._stack[-1*num:]
                return list(reversed(popped_list))
        except Exception as e:
            print('stack already empty')

    def top(self):
        if self._stack:
            return self._stack[-1]
        else:
            return ''
    def show(self):
        return self._stack
def return_all_top_crateids(filename=None):
    try:

        stack_initial_input_map = {}
        result_list = []

        with open(filename, 'r') as f:
            initial_position, steps = f.read().split('\n\n')
        
        initial_position = initial_position.split('\n')
        steps = steps.split('\n')

        no_of_stacks = len(initial_position[-1].strip().split('  '))

        for i in range(no_of_stacks):
            stack_initial_input_map[i] = []

        for input_line in initial_position[0:-1]:
            crates_per_line = re.findall('^\s\s\s|\s\s\s\s|\[\w\]', input_line)

            for crate in enumerate(crates_per_line):
                # print(crate)
                if crate[1].strip():
                    stack_initial_input_map[crate[0]].append(crate[1].strip())
                    # print(crate)
                
        for key, value in stack_initial_input_map.items():
            stack_initial_input_map[key] = Stack(list(reversed(value)))

        for action in steps:
            crate_count, from_stack, to_stack = tuple(map(int, re.findall('\d{1,}', action)))
            
            crate_list = stack_initial_input_map[from_stack-1].pop(crate_count)
            stack_initial_input_map[to_stack-1].push(crate_list)

        for stack in stack_initial_input_map.keys():
            result_list.append(stack_initial_input_map[stack].top())
        
        result_string = ' '.join(result_list)
        return re.sub('\s|[\[\]]', '', result_string)
        # print('done')
    except Exception as e:
        print("error in return_all_top_crateids fn", str(e))

def return_all_top_createids_9001(filename=None):
    try:

        stack_initial_input_map = {}
        result_list = []

        with open(filename, 'r') as f:
            initial_position, steps = f.read().split('\n\n')
        
        initial_position = initial_position.split('\n')
        steps = steps.split('\n')

        no_of_stacks = len(initial_position[-1].strip().split('  '))

        for i in range(no_of_stacks):
            stack_initial_input_map[i] = []

        for input_line in initial_position[0:-1]:
            crates_per_line = re.findall('^\s\s\s|\s\s\s\s|\[\w\]', input_line)

            for crate in enumerate(crates_per_line):
                # print(crate)
                if crate[1].strip():
                    stack_initial_input_map[crate[0]].append(crate[1].strip())
                    # print(crate)
                
        for key, value in stack_initial_input_map.items():
            stack_initial_input_map[key] = Stack(list(reversed(value)))

        for action in steps:
            crate_count, from_stack, to_stack = tuple(map(int, re.findall('\d{1,}', action)))
            
            crate_list = stack_initial_input_map[from_stack-1].pop(crate_count)
            stack_initial_input_map[to_stack-1].push(list(reversed(crate_list)))

        for stack in stack_initial_input_map.keys():
            result_list.append(stack_initial_input_map[stack].top())
        
        result_string = ' '.join(result_list)
        return re.sub('\s|[\[\]]', '', result_string)
        # print('done')
    except Exception as e:
        print("error in return_all_top_crateids fn", str(e))


if __name__=="__main__":
    input = './sample/sample5.txt'
    input = './input/advent_of_code_day5_input.txt'

    # result = return_all_top_crateids(filename=input)
    result = return_all_top_createids_9001(filename=input)

    print(result)