import re
import copy

class Node:
    def __init__(self, name, files, dirs, parent):
        self._name = name
        self._files = []
        self._dirs = dict()
        self._size = 0
        self._parent = None
        if files: self._files = files
        if dirs: self._dirs = dirs
        if parent: self._parent = parent

    def get_child_directory(self, name):
        return self._dirs.get(name, None)
    def set_child_node(self, name, node_instance):
        self._dirs[name] = node_instance
    
    # def get_all_child_nodes(self):
    #     return self._dirs.values()

    def set_parent(self, parent):
        self._parent = parent
    def get_parent(self):
        return self._parent

    def get_files_and_dirs(self):
        return (self._files, self._dirs)

    def set_files_and_dirs(self, files, dirs):
        self._files = list(set(self._files).union(set(files)))
        self._dirs = {**self._dirs, **dirs}

    def add_file(self, file):
        if file:
            self._files.append(file)
    def __repr__(self):
        # subfolders = '\n'.join([f'  \\{x}' for x in self._dirs.keys()])
        # return self._name+'\n'+subfolders
        return self._name

def calculate_total_directory_size_sub_100000(filename=None):
    try:
        pass
    except Exception as e:
        print("error in calculate_total_directory_size_sub_100000 fn", str(e))

def construct_file_tree(filename=None):
    try:
        root_node = None
        current_directory = None
        current_dir_name = ''
        with open(filename, 'r') as f:
            commands = re.split(r'^\$|\n\$',f.read().strip())
        
        for command in commands[1:]:
            if 'cd' == command.strip().split()[0]:
                if '/' in command:
                    current_dir_name = 'root'
                    if root_node is None:
                        current_directory = Node(current_dir_name, None, None, None)
                        root_node = (current_directory,)[0]
                elif '..' in command:
                    current_directory = current_directory.get_parent()
                else:
                    current_dir_name = command.strip().split()[-1]
                    if current_directory.get_child_directory(name=current_dir_name) is None:
                        new_node = Node(current_dir_name, None, None, current_directory)
                        current_directory.set_child_node(current_dir_name, new_node)
                        current_directory = new_node
                    else:
                        current_directory = current_directory.get_child_directory(current_dir_name)
            
            elif 'ls' == command.strip().split()[0]:
                files = []
                directories = dict()
                for file_item in command.strip().split('\n')[1:]:
                    if re.match(r'dir(?=\s)', file_item):
                        directories[file_item.split()[1]] = None
                    elif re.match(r'\d{1,}(?=\s)', file_item):
                        files.append((file_item.split()[0], file_item.split()[1]))

                current_directory.set_files_and_dirs(files, directories)
            # print('ab')
        return root_node
        # print('done')
    except Exception as e:
        print("error in construct_file_tree fn", str(e))
def traverse_tree_nodes(root_node=None):
    ''' Traversing nodes in DFS fashion.'''
    try:
        folder_size_dict = dict()
        visited_dict = dict()
        _stack = [root_node]
        sub_100k_size = 0
        while(_stack):
            current_node = _stack.pop()
            try:
                all_files, all_children = current_node.get_files_and_dirs()
            except Exception as e:
                visited_dict[current_node] = 1
                folder_size_dict[current_node] = 0
                continue

            if current_node not in visited_dict:
                _stack.append(current_node)
                if all_children:
                    _stack.extend(all_children.values())
                visited_dict[current_node] = 1
                continue

            if current_node in visited_dict:
                folder_size =  0
                print(current_node._name)
                for file in all_files:
                    folder_size += int(file[0])
                if all_children is None:
                    folder_size_dict[current_node] = folder_size
                else:
                    for child in all_children.values():
                        folder_size += folder_size_dict[child]
                    folder_size_dict[current_node] = folder_size

        for size in folder_size_dict.values():
            if size <= 100000:
                sub_100k_size += size

        total_size = max(folder_size_dict.values())
        if total_size == 0:
            return sub_100k_size, 0
        else:
            all_dirs_sizes_candidate_for_deletion = list(filter(lambda x: x >= total_size-40000000, folder_size_dict.values()))
            return sub_100k_size, min(all_dirs_sizes_candidate_for_deletion)

    except Exception as e:
        print("error in traverse_tree_nodes fn",str(e))
if __name__=="__main__":
    input = './sample/sample7.txt'
    input = './input/advent_of_code_day7_input.txt'

    file_tree_root_node = construct_file_tree(filename=input)
    result_part_1, result_part_2 = traverse_tree_nodes(file_tree_root_node)

    # result = calculate_total_directory_size_sub_100000(filename=input)

    print('done')