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

day_5()