def get_sum_of_all_positions_of_tail(filename=None):
    try:
        head_initial, head_final = [[0, 0], [0, 0]]
        tail_initial, tail_final = [[0, 0], [0, 0]]
        tail_position_set = {(0,0)}
        with open(filename, 'r') as f:
            all_input = f.read().strip().split('\n')
        for input in all_input:
            head_initial = head_final[:]
            tail_initial = tail_final[:]
            direction, displacement = input.strip().split()
            displacement = int(displacement)
            if direction == 'R':
                head_final[0] += displacement
            elif direction == 'L':
                head_final[0] -= displacement
            elif direction == 'D':
                head_final[1] -= displacement
            elif direction == 'U':
                head_final[1] += displacement
            
            if not is_neighbour_position(head_final, tail_initial):
                if direction in ('U', 'D'):
                    tail_initial[0] = head_final[0]
                    tail_final[0] = tail_initial[0]
                    if direction == 'U':
                        tail_initial[1] += 1
                        tail_final[1] = head_final[1] - 1

                        for i in range(tail_initial[1], tail_final[1]+1):
                            tail_position_set.add((tail_initial[0], i))
                    else:
                        tail_initial[1] -= 1
                        tail_final[1] = head_final[1] + 1

                        for i in range(tail_final[1], tail_initial[1] + 1):
                            tail_position_set.add((tail_initial[0], i))
                else:
                    tail_initial[1] = head_final[1]
                    tail_final[1] = tail_initial[1]
                    if direction == 'R':
                        tail_initial[0] += 1
                        tail_final[0] = head_final[0] - 1

                        for i in range(tail_initial[0], tail_final[0] + 1):
                            tail_position_set.add((i, tail_initial[1]))
                    else:
                        tail_initial[0] -= 1
                        tail_final[0] = head_final[0] + 1

                        for i in range(tail_final[0], tail_initial[0] + 1):
                            tail_position_set.add((i, tail_initial[1]))

            # print('done')
        return len(tail_position_set)
    except Exception as e:
        print("error in get_sum _of_all_positions_of_tails fn", str(e))
def get_all_positions_of_nth_follower_node(filename=None):
    try:
        all_positions_dict = {}
        head_all_positions = [[0,0]]
        follower_position_1 = [[0,0]]
        head_position = None
        with open(filename, 'r') as f:
            all_input = f.read().strip().split('\n')

        for input in all_input:
            head_position = head_all_positions[-1][:]
            direction, displacement = input.strip().split()
            displacement = int(displacement)
            if direction == 'R':
                for i in range(1, displacement + 1):
                    head_all_positions.append([head_position[0]+i, head_position[1]])
            elif direction == 'L':
                for i in range(1, displacement + 1):
                    head_all_positions.append([head_position[0]-i, head_position[1]])
            elif direction == 'D':
                for i in range(1, displacement + 1):
                    head_all_positions.append([head_position[0], head_position[1]-i])
            elif direction == 'U':
                for i in range(1, displacement + 1):
                    head_all_positions.append([head_position[0], head_position[1]+i])

        all_positions_dict['H'] = head_all_positions[:]
        for i in range(1, 10):
            for position in head_all_positions:
                if not is_neighbour_position(position, follower_position_1[-1]):
                    new_follower_position = get_next_following_position(position, follower_position_1[-1])
                    follower_position_1.append(new_follower_position[:])
            
            head_all_positions = follower_position_1[:]
            follower_position_1 = [[0,0]]
            all_positions_dict[i] = head_all_positions[:]
            print('a')
        print('done')
    except Exception as e:
        print("error in get_all_positions_of_nth_follower_node fn", str(e))

def get_next_following_position(leader, follower):
    '''Return the coord. of next position of tail-gaiting node'''
    final_position = [0, 0]
    if leader[0] - follower[0] in (-1, 0, 1):
        if leader[1] - follower[1] in (-2, 2):
            final_position[0] = leader[0]
            final_position[1] = follower[1] + (leader[1]-follower[1])//2
        else:
            print(f'this cannot happen {leader}---{follower}')
    else:
        if leader[1] - follower[1] in (-1, 0, 1):
            final_position[0] = follower[0] + (leader[0] - follower[0])//2
            final_position[1] = leader[1]
        else:
            final_position[0] = follower[0] + (leader[0] - follower[0])//2
            final_position[1] = follower[1] + (leader[1] - follower[1])//2
    return final_position
def is_neighbour_position(head, tail):
    '''Whether is the two coordinates are adjacent incl. diagonally.'''
    xh, yh = head
    xt, yt = tail
    if (xh - xt) in (-1, 0, 1) and (yh - yt) in (-1, 0, 1):
        return True
    else:
        return False

if __name__=="__main__":
    # input = './sample/sample9.txt'
    # input = './sample/sample9_2.txt'
    # input = './sample/sample9_3.txt'
    input = './input/advent_of_code_day9_input.txt'    

    # result = get_sum_of_all_positions_of_tail(filename=input)
    result = get_all_positions_of_nth_follower_node(filename=input)

    print(result)