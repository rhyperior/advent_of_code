import re

ROW_COUNT = None
COL_COUNT = None
height_map = None
def return_hillclimb_step_count(filename=None):
    try:
        global ROW_COUNT
        global COL_COUNT
        global height_map
        height_map = []
        map_graph = {}
        destination_cell = None
        starting_cell = None
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n')
        for input in all_inputs:
            height_map.append(re.findall('\w', input))
        
        # height_map[0][0] = 'a'

        ROW_COUNT = len(height_map)
        COL_COUNT = len(height_map[0])

        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                if height_map[row][col] == 'E':
                    destination_cell = (row, col)
                    height_map[row][col] = 'z'
                if height_map[row][col] == 'S':
                    starting_cell = (row, col)
                    height_map[row][col] = 'a'

        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):

                current = height_map[row][col]
                if row == 2 and col == 4:
                    print('o yeah')
                _list =  list(filter(graph_edge_filter, [(current, (row-1, col)), (current, (row+1, col)), (current, (row, col-1)), (current, (row, col+1))]))
                edges = []
                for edge in _list:
                    edges.append(str((edge[1][0], edge[1][1])))
                map_graph[str((row, col))] = edges[:]
                
        res = bfs_traversal(map_graph, str(starting_cell), str(destination_cell))
        print('done')
    except Exception as e:
        print("error in return_hummclimb_step_count fn", str(e))

def graph_edge_filter(args):
    current, cell = args
    if cell[0] >= 0 and cell[0] < ROW_COUNT and cell[1] >= 0 and cell[1] < COL_COUNT:
        # if ord(height_map[cell[0]][cell[1]]) - ord(current) in (-1, 0 , 1):
        if ord(height_map[cell[0]][cell[1]]) <= ord(current) + 1:
            return True
    return False
def bfs_traversal(graph=None, starting_node = None, target_node = None):
    try:
        _steps = 0
        visited_nodes = {starting_node: 0}
        _queue = [starting_node]
        current_node = None
        count = 0
        levelwise_queue = []
        while(True):
            if current_node == target_node:
                print('reached! nigger.')
                break
            count += 1
            # levelwise_queue = []
            # print(f'inside bfs {count}')
            current_node = _queue.pop(0)
            adjacent_nodes = graph[current_node]
            non_visited_adjacent = list(filter(lambda x: x not in visited_nodes, adjacent_nodes))
            levelwise_queue.extend(non_visited_adjacent)
            for node in non_visited_adjacent:
                visited_nodes[node] = _steps + 1
            # print(current_node)
        
            if not _queue:
                _queue.extend(levelwise_queue)    
                _steps += 1
                levelwise_queue.clear()
                print(_steps)

        return visited_nodes[target_node]
    except Exception as e:
        print("error in bfs_traversal fn", str(e))
        return -1
def nearest_lowest_starting_point(filename=None):
    try:
        global ROW_COUNT
        global COL_COUNT
        global height_map
        height_map = []
        map_graph = {}
        destination_cell = None
        starting_cell = None
        all_lowest_points_distances = []
        with open(filename, 'r') as f:
            all_inputs = f.read().strip().split('\n')
        for input in all_inputs:
            height_map.append(re.findall('\w', input))
        
        # height_map[0][0] = 'a'

        ROW_COUNT = len(height_map)
        COL_COUNT = len(height_map[0])

        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                if height_map[row][col] == 'E':
                    destination_cell = (row, col)
                    height_map[row][col] = 'z'
                if height_map[row][col] == 'S':
                    starting_cell = (row, col)
                    height_map[row][col] = 'a'

        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                current = height_map[row][col]
                
                _list =  list(filter(graph_edge_filter, [(current, (row-1, col)), (current, (row+1, col)), (current, (row, col-1)), (current, (row, col+1))]))
                edges = []
                for edge in _list:
                    edges.append(str((edge[1][0], edge[1][1])))
                map_graph[str((row, col))] = edges[:]
                
        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                if height_map[row][col] == 'a':
                    starting_cell = (row, col)
                    all_lowest_points_distances.append(bfs_traversal(map_graph, str(starting_cell), str(destination_cell)))
        
        a_set = set()
        [a_set.add(i) for i in all_lowest_points_distances]
        a_set.remove(-1)
        return min(a_set)
        print('done')
    except Exception as e:
        print("error in nearest_lowest_starting_point fn", str(e))
if __name__=="__main__":
    input = './sample/sample12.txt'
    input = './input/advent_of_code_day12_input.txt'

    # result = return_hillclimb_step_count(filename=input)
    result = nearest_lowest_starting_point(filename=input)

    print(result)