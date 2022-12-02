
def calculate_total_score(filename=None):
    try:
        draw_map = {'X':'A' , 'Y':'B', 'Z':'C'}
        win_map = {'X':'C' , 'Y':'A', 'Z':'B'}
        lose_map = {'X':'B' , 'Y':'C', 'Z':'A'}

        score_map = {'X': 1, 'Y':2, 'Z':3}
        score = 0
        with open(filename, 'r') as f:
            all_rounds = f.read().strip().split('\n')

        for round in all_rounds:
            opponent, self = round.split(' ')
            if opponent == draw_map[self]:
                score += score_map[self] + 3
            elif opponent == win_map[self]:
                score += score_map[self] + 6
            elif opponent == lose_map[self]:
                score += score_map[self]

        return score
    except Exception as e:
        print("error in calculate_total_score fn", str(e))

def calculate_correct_total_score(filename=None):
    try:
        draw_map = {'X':'A' , 'Y':'B', 'C':'C'}
        win_map = {'A':'C' , 'B':'A', 'C':'B'}
        lose_map = {'A':'B' , 'B':'C', 'C':'A'}

        score_map = {'A': 1, 'B':2, 'C':3}
        score = 0
        with open(filename, 'r') as f:
            all_rounds = f.read().strip().split('\n')

        for round in all_rounds:
            opponent, self = round.split(' ')
            
            if self == 'X':
                score += score_map[win_map[opponent]]
            elif self == 'Z':
                score += score_map[lose_map[opponent]] + 6
            else:
                score += score_map[opponent] + 3

        return score
    except Exception as e:
        print("error in calculate_total_score fn", str(e))

    
if __name__=="__main__":
    input = 'sample2.txt'
    input = 'advent_of_code_day2_input.txt'

    # score = calculate_total_score(filename=input)
    score = calculate_correct_total_score(filename=input)
    print(score)
