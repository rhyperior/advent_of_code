import re

def calculate_priorities_sum(filename=None):
    try:
        total_priority = 0
        with open(filename, 'r') as f:
            all_runsacks = f.read().strip().split('\n')

            for runsack in all_runsacks:
                # splitting each input line by half , for each runsack
                first_set = set(runsack[0:len(runsack)//2])
                second_set = set(runsack[len(runsack)//2:])

                common_item = first_set.intersection(second_set).pop()

                if ord(common_item) >= 65 and ord(common_item) <= 90:
                    total_priority += ord(common_item) - 38
                elif ord(common_item) >= 97 and ord(common_item) <= 122:
                    total_priority += ord(common_item) - 96

        return total_priority
        # print(all_runsacks)
    except Exception as e:
        print("error in calculate_priorities_sum", str(e))

def calculate_badge_priorities_sum(filename=None):
    try:
        total_priority = 0
        with open(filename, 'r') as f:
            # for spliting the input in three lines each
            regex = r'\w{1,}\n\w{1,}\n\w{1,}\n|\w{1,}\n\w{1,}\n\w{1,}$'

            all_runsacks = re.findall(regex, f.read().strip())

            # print(all_runsacks)
            for runsack in all_runsacks:
                first_elf, second_elf, third_elf = runsack.strip().split('\n')
                first_set = set(first_elf)
                second_set = set(second_elf)
                third_set = set(third_elf)

                common_item = first_set.intersection(second_set, third_set).pop()

                if ord(common_item) >= 65 and ord(common_item) <= 90:
                    total_priority += ord(common_item) - 38
                elif ord(common_item) >= 97 and ord(common_item) <= 122:
                    total_priority += ord(common_item) - 96

        return total_priority
        # print(all_runsacks)
    except Exception as e:
        print("error in calculate_badge_priorities_sum", str(e))

if __name__=="__main__":
    input = './sample/sample3.txt'
    input = './input/advent_of_code_day3_input.txt'

    # result = calculate_priorities_sum(filename=input)
    result = calculate_badge_priorities_sum(filename=input)
    print(result)