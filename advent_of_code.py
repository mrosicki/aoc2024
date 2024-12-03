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


day_3()