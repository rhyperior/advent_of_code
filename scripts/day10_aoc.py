import re

def return_signal_strenths_in_range_of_cpucycles(filename=None):
    try:
        # cycles = [1,2, 3,4, 5]
        cycles = [19, 20, 59, 60, 99, 100, 139, 140, 179, 180, 181, 219, 220, 221]
        cycles = [20, 60,100, 140, 180, 220]
        # cycles = [140, 180, 220]
        _xvalues = []
        cycle = 0
        var_x = 1
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n')
        for input in all_inputs:
            # print(input)
            if 'noop' == input.strip().split()[0]:
                cycle += 1

                if cycle in cycles:
                    _xvalues.append(var_x * cycle)
                    print(f'{input}  --{instruction}--{cycle}')
                    # print(f'{var_x}--{cycle}')

            else:
                instruction_cycle = 2
                for instruction in range(instruction_cycle):
                    cycle += 1
                    
                    if cycle in cycles:
                        _xvalues.append(var_x * cycle)
                        print(f'{input}  --{instruction}--{cycle}')
                        # print(f'{var_x}--{cycle}')

                    if instruction == instruction_cycle - 1:
                        var_x += int(input.strip().split()[1])
        
        return sum(_xvalues)
    except Exception as e:
        print("error in return_signal_strengths_in_range_of_cpucycles fn", str(e))

def glow_pixel_based_on_cpu_instruction(filename=None):
    try:
        cycle = 0
        var_x = 1
        sprite_pos = 1
        current_pixel_pos = 0
        pixel_print = []
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n')
        
        for input in all_inputs:
            if 'noop' == input.strip().split()[0]:
                # first glow the pixel as sprite_pos and cycle % 40
                # update the cycle.
                current_pixel_pos = cycle % 40
                if sprite_pos - current_pixel_pos in (-1, 0, 1):
                    pixel_print.append('#')
                else:
                    pixel_print.append('.')
                cycle +=1

            else:
                instructions = 2  # Add to register takes two instruction cycles to complete.

                for i in range(instructions):
                    # first glow led acc to sprite_pos and cycle % 40
                    # update x_value acc to cycle (update after two)
                    # update sprite position acc to x_value
                    #  then update cycle
                    current_pixel_pos = cycle % 40
                    if sprite_pos - current_pixel_pos in (-1, 0, 1):
                        pixel_print.append('#')
                    else:
                        pixel_print.append('.')

                    if i == instructions - 1:
                        var_x += int(input.strip().split()[1])
                        sprite_pos = var_x
                    cycle += 1
        
        pixel_print = ''.join(pixel_print)
        return re.findall('[\.\#]{40}', pixel_print)
    except Exception as e:
        print("error in glow_pixed_based_on_cpu_instruction fn", str(e))
if __name__=="__main__":
    input = './sample/sample10.txt'
    input = './sample/sample10_2.txt'
    input = './input/advent_of_code_day10_input.txt'

    # result = return_signal_strenths_in_range_of_cpucycles(filename=input)
    result = glow_pixel_based_on_cpu_instruction(filename=input)

    print(result)
    # ans - PHLHJGZA