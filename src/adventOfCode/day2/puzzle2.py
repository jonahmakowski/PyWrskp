def report_check(reports):
    safe = 0
    nots = []
    for ind, report in enumerate(reports):
        if is_safe(report):
            safe += 1
        else:
            nots.append(ind)
    return safe, nots

def is_safe(report):
    if check_report(report):
        return True
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]
        if check_report(temp):
            return True
    return False

def check_report(report):
    if len(report) < 2:
        return False
    status = False
    if report[0] < report[1]:
        typ = 1
    elif report[0] > report[1]:
        typ = -1
    else:
        return False
    
    prev_num = None
    for num in report:
        if prev_num is not None:
            if 1 <= abs(num-prev_num) <= 3:
                if num < prev_num and typ == -1:
                    status = True
                elif num > prev_num and typ == 1:
                    status = True
                else:
                    return False
            else:
                return False
        prev_num = num
    return status

def do_challenge():
    with open('input.txt') as f:
        lines = f.readlines()
    
    reports = []
    for line in lines:
        report = []
        for num in line.strip().split():
            report.append(int(num))
        reports.append(report)

    safe, nots = report_check(reports)

    return safe

print(do_challenge())