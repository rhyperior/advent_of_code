def return_first_marker_position(filename=None):
    try:
        unique_test_set = None
        with open(filename, 'r') as f:
            character_stream = f.read().strip()

        for i in range(len(character_stream)-3):
            unique_test_set = set(character_stream[i:i+4])
            
            if len(unique_test_set) == 4:
                return i+4
        
        return 0
    except Exception as e:
        print("error in return_first_maker_position fn", str(e))

def return_first_message_marker_position(filename=None):
    try:
        unique_test_set = None
        with open(filename, 'r') as f:
            character_stream = f.read().strip()

        for i in range(len(character_stream)-13):
            unique_test_set = set(character_stream[i:i+14])
            
            if len(unique_test_set) == 14:
                return i+14
        
        return 0
    except Exception as e:
        print("error in return_first_maker_position fn", str(e))

if __name__=="__main__":
    input = "./sample/sample6.txt"
    input = "./input/advent_of_code_day6_input.txt"

    # result = return_first_marker_position(filename=input)
    result = return_first_message_marker_position(filename=input)

    print(result)