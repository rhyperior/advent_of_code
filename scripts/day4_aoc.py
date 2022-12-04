def return_fully_enclosing_pairs(filename=None):
    try:
        
        fully_contained_pairs_count = 0

        with open(filename, 'r') as f:
            all_pairs = f.read().strip().split('\n')

            for pair in all_pairs:
                first_elf, second_elf = pair.split(',')

                first_elf_sections = list(map(int, first_elf.split('-')))
                second_elf_sections = list(map(int, second_elf.split('-')))

                # first_elf_section_difference = first_elf_sections[1] - first_elf_sections[0]
                # second_elf_section_difference = second_elf_sections[1] - second_elf_sections[0]

                # big_section = max(first_elf_section_difference, second_elf_section_difference)
                # small_section = min(first_elf_section_difference, second_elf_section_difference)

                if first_elf_sections[0] <= second_elf_sections[0] and first_elf_sections[1] >= second_elf_sections[1]:
                    fully_contained_pairs_count += 1
                elif second_elf_sections[0] <= first_elf_sections[0] and second_elf_sections[1] >= first_elf_sections[1]:
                    fully_contained_pairs_count += 1
            
        return fully_contained_pairs_count
    except Exception as e:
        print("error in return_fullly_enclosing_pairs fn", str(e))

def return_partially_overlapping_pair_count(filename=None):
    try:
        
        fully_contained_pairs_count = 0

        with open(filename, 'r') as f:
            all_pairs = f.read().strip().split('\n')

            for pair in all_pairs:
                first_elf, second_elf = pair.split(',')

                first_elf_sections = list(map(int, first_elf.split('-')))
                second_elf_sections = list(map(int, second_elf.split('-')))

                # first_elf_section_difference = first_elf_sections[1] - first_elf_sections[0]
                # second_elf_section_difference = second_elf_sections[1] - second_elf_sections[0]

                # big_section = max(first_elf_section_difference, second_elf_section_difference)
                # small_section = min(first_elf_section_difference, second_elf_section_difference)

                if second_elf_sections[0] <= first_elf_sections[1] and second_elf_sections[0] >= first_elf_sections[0]:
                    fully_contained_pairs_count += 1
                elif first_elf_sections[0] <= second_elf_sections[1] and first_elf_sections[0] >= second_elf_sections[0]:
                    fully_contained_pairs_count += 1
            
        return fully_contained_pairs_count
    except Exception as e:
        print("error in return_fullly_enclosing_pairs fn", str(e))

if __name__=="__main__":
    input = './sample/sample4.txt'
    input = './input/advent_of_code_day4_input.txt'

    # result = return_fully_enclosing_pairs(filename=input)
    result = return_partially_overlapping_pair_count(filename=input)
    
    print(result)