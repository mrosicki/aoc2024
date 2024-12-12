def day_1():
    with open("input", "r") as file:
        data = file.readlines()
    list1 = []
    list2 = []
    for line in data:
        splits = line.split("   ")
        v1 = int(splits[0])
        v2 = int(splits[1].replace("\n", ""))
        list1.append(v1)
        list2.append(v2)

    list1.sort()
    list2.sort()
    distances = []
    for v1, v2 in zip(list1, list2):
        distances.append(abs(v1-v2))
    print(sum(distances))
    total_score = 0
    for elem in list1:
        count = len([copy for copy in list2 if copy == elem])
        similarity_score = elem * count
        total_score += similarity_score

    print(total_score)


def day_2():
    report_list = []
    safe_reports_count = 0
    with open("input", "r") as file:
        data = file.readlines()

    for report in data:
        parsed_report = [int(level) for level in report.split(" ")]
        report_list.append(parsed_report)
    
    def test_asc_desc(report):
        desc = report.copy()
        desc.sort(reverse=True)
        asc = report.copy()
        asc.sort(reverse=False)
        if report not in [desc, asc]:
            return False
        return True
    
    def test_diff(report):
        for i in range(len(report) -1):
            if abs(report[i] - report[i+1]) < 1:
                return False
            if abs(report[i] - report[i+1]) > 3:
                return False
            if report[i] == report[i+1]:
                return False
        return True
    
    
    safe_reports_count = len([report for report in report_list if test_asc_desc(report) and test_diff(report)])
    print(safe_reports_count)
    dampened_safe_reports_count = 0

    for report in report_list:
        for i in range(len(report)):
            copy = report.copy()
            del copy[i]
            if test_asc_desc(copy) and test_diff(copy):
                dampened_safe_reports_count +=1
                break
            
    print(dampened_safe_reports_count)

def day_3():
    import re
    with open("input", "r") as file:
        data = file.readlines()
    total = 0
    for line in data:
        matches = re.findall("do\(\)|mul\(\d+,\d+\)|don't\(\)", line)
        for match in matches:
            if match[:3] == "mul":
                v1 = int(match.split(",")[0][4:])
                v2 = int(match.split(",")[1][:-1])
                total += v1 * v2
    print(total)    

    enable_multiplier = 1
    total = 0
    for line in data:
        matches = re.findall("do\(\)|mul\(\d+,\d+\)|don't\(\)", line)
        for match in matches:
            if match[:3] == "mul":
                v1 = int(match.split(",")[0][4:])
                v2 = int(match.split(",")[1][:-1])
                total += v1 * v2 * enable_multiplier
            if match == "do()":
                enable_multiplier = 1
            if match == "don't()":
                enable_multiplier = 0
    print(total)


def day_4():
    with open("input", "r") as file:
        data = file.readlines()

    def print_data(data):
        for line in data:
            print(line.replace("\n", ""))


    def check_direction(row, col, data, direction_vector):
        if row + direction_vector[1] * 3 > len(data)-1:
            return False
        if row + direction_vector[1] * 3 < 0:
            return False
        if col + direction_vector[0] * 3 > len(data[row])-1:
            return False
        if col + direction_vector[0] * 3 < 0:
            return False

        word = [data[row+direction_vector[1]*i][col+direction_vector[0]*i] for i in range(4)]

        if word != ["X", "M", "A", "S"]:
            return False
        else:
            return True
        

    
    def check_word(row, col, data):
        if data[row][col] != "X":
            return 0

        matches = 0
        
        N = (0, 1)
        NE = (1, 1)
        E = (1, 0)
        SE = (1, -1)
        S = (0, -1)
        SW = (-1, -1)
        W = (-1, 0)
        NW = (-1, 1)
        for direction in [N,NE,E,SE,S,SW,W,NW]:
            if check_direction(row,col,data,direction):
                matches+=1
        
        return matches

    total = 0

        
    for row in range(len(data)):
        for col in range(len(data[row])):
            total += check_word(row,col,data)

    print(total)

    def check_square(row, col, data):
        if data[row][col] not in ["M", "S"]:
            return False
        if data[row+1][col+1] != "A":
            return False
        if set(["M", "S"]) == set([data[row][col], data[row+2][col+2]]) and set(["M", "S"]) == set([data[row+2][col], data[row][col+2]]):
            return True
        
    
    total = 0

        
    for row in range(len(data)-2):
        for col in range(len(data[row])-2):
            if check_square(row,col,data):
                total += 1

    print(total)
                


def day_5():
    def check_rule(update: list, rule: tuple):
        try:
            i1 = update.index(rule[0])
            i2 = update.index(rule[1])
        except ValueError:
            return True
        else:
            if i1 < i2:
                return True
            else:
                return False


    with open("input", "r") as file:
        data = file.readlines()
    rules = [tuple(line.replace("\n", "").split("|")) for line in data if "|" in line]
    updates = [list(line.replace("\n", "").split(",")) for line in data if "," in line]
    invalid_updates = []
    sum_of_middles = 0
    for update in updates:
        is_valid = True
        for rule in rules:
            if not check_rule(update, rule):
                is_valid = False
        if is_valid:
            sum_of_middles += int(update[(len(update)//2)])
        else:
            invalid_updates.append(update)

    print(sum_of_middles)


    sum_of_middles = 0
    for update in invalid_updates:
        for i in range(len(update)):
            for rule in rules:
                if not check_rule(update, rule):
                    update[update.index(rule[0])], update[update.index(rule[1])] =  update[update.index(rule[1])], update[update.index(rule[0])]
        
        sum_of_middles += int(update[(len(update)//2)])
    print(sum_of_middles)

def day_6():
    import os
    with open("input", "r") as file:
        data = file.readlines()

    original_board = [[cell for cell in line] for line in data]

    def copy_board(board):
        copy = [row.copy() for row in board]
        return copy
    


    def print_board(board):
        for row in board:
            for cell in row:
                print(cell, end="")

    
    def get_next_guard_step(data, guard_row, guard_col):
        directions_dict = {
            # guard: (row_diff, col_diff)
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0,-1),
        }
        guard_directions = ["^",">","v","<"]
        guard = data[guard_row][guard_col]
        # return None -> guard leaves map
        if 0 > guard_row + directions_dict[guard][0] or guard_row + directions_dict[guard][0] > len(data)-1:
            return None
        if 0 > guard_col + directions_dict[guard][1] or guard_col + directions_dict[guard][1]> len(data[guard_row])-1:
            return None
        # return string -> guard rotates
        if data[guard_row + directions_dict[guard][0]][guard_col + directions_dict[guard][1]] == "#":
            return guard_directions[((guard_directions.index(guard)+1) % 4)]
        return (guard_row + directions_dict[guard][0], guard_col + directions_dict[guard][1])

    initial_guard_row = [i for i, line in enumerate(data) if "^" in line][0]
    initial_guard_col = data[initial_guard_row].index("^")           

        

    guard_row = initial_guard_row
    guard_col = initial_guard_col

    prev_move = None
    original_cell_content = None
    board = copy_board(original_board)

    while get_next_guard_step(board, guard_row, guard_col) is not None:
        next_step = get_next_guard_step(board, guard_row, guard_col)
        if isinstance(next_step, str):
            board[guard_row][guard_col] = next_step
            prev_move = "rotate"
        if isinstance(next_step, tuple):
            if prev_move == "rotate":
                step_symbol = "+"
            else:
                step_symbol = "|" if board[guard_row][guard_col] in ["^", "v"] else "-"
                if set(["|", "-"]) == set([step_symbol, original_cell_content]):
                    step_symbol = "+"
            original_cell_content = board[next_step[0]][next_step[1]]
            board[next_step[0]][next_step[1]] = board[guard_row][guard_col]

            board[guard_row][guard_col] = step_symbol
            guard_row, guard_col = next_step[0], next_step[1]
            prev_move = "move"

    
    cells_visited = 0
    for row in board:
        for cell in row:
            if cell in ["|", "+", "-", "v", "^", "<", ">"]:
                cells_visited +=1
    
    print(cells_visited)

    # abhorrent performance but I can't think of a smarter way to do this

    num_of_cells = len(original_board) * (len(original_board[0])-1)


    valid_boards = 0
    board_no = 0
    for row in range(len(original_board)):
        for col in range(len(original_board[row])-1):
            board_no +=1
            print(f"{board_no}/{num_of_cells}")
            cycle = 0
            board = copy_board(original_board)

            if board[row][col] == "#" or (row == initial_guard_row and col == initial_guard_col):
                continue
            else:
                board[row][col] = "#"
            initial_guard_row = [i for i, line in enumerate(data) if "^" in line][0]
            initial_guard_col = data[initial_guard_row].index("^")           

                

            guard_row = initial_guard_row
            guard_col = initial_guard_col

            prev_move = None
            original_cell_content = None

            while get_next_guard_step(board, guard_row, guard_col) is not None:
                cycle+=1
                next_step = get_next_guard_step(board, guard_row, guard_col)
                if isinstance(next_step, str):
                    board[guard_row][guard_col] = next_step
                    prev_move = "rotate"
                if isinstance(next_step, tuple):
                    if prev_move == "rotate":
                        step_symbol = "+"
                    else:
                        step_symbol = "|" if board[guard_row][guard_col] in ["^", "v"] else "-"
                        if set(["|", "-"]) == set([step_symbol, original_cell_content]):
                            step_symbol = "+"
                    original_cell_content = board[next_step[0]][next_step[1]]
                    board[next_step[0]][next_step[1]] = board[guard_row][guard_col]

                    board[guard_row][guard_col] = step_symbol
                    guard_row, guard_col = next_step[0], next_step[1]
                    prev_move = "move"


                
                if cycle > num_of_cells:
                    print_board(board)
                    print()
                    valid_boards+=1
                    break
    print(valid_boards)
            



def day_7():
    from itertools import product
    with open("input","r") as f:
        data = f.readlines()

    add = lambda a,b: a+b
    mul = lambda a,b: a*b
    con = lambda a,b: int(str(a)+str(b))

    total = 0
    for line in data:
        test_value, inputs = line.replace("\n", "").split(":")
        test_value = int(test_value)
        inputs = [int(value) for value in inputs.split(" ") if value]
        operations = [add, mul, con]
        num_of_operations = (len(inputs)-1)
        operator_combos = list(product(*[operations for i in range(num_of_operations)]))
        value_possible = False
        for combo in operator_combos:
            t = inputs[0]
            for i, operation in enumerate(combo):
                t = operation(t, inputs[i+1])
            if t == test_value:
                value_possible = True
                break
        
        if value_possible:
            total += t

    print(total)
        

def day_9():
    with open("input", "r") as file:
        data = file.readlines()

day_6()