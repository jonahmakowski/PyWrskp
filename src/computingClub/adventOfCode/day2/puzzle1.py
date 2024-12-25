def do_challenge():
    with open('input.txt') as f:
        lines = f.readlines()
    
    reports = []
    for line in lines:
        report = []
        for num in line.strip().split():
            report.append(int(num))
        reports.append(report)
    
    safe = 0

    for ind, report in enumerate(reports):
        status = False
        if report[0] < report[1]:
            typ = 1
            #print('Accending')
        elif report[0] > report[1]:
            typ = -1
            #print('Decending')
        else:
            #print('First two are the same {} and {}'.format(report[0], report[1]))
            continue
        
        prev_num = None
        for num in report:
            if prev_num is not None:
                if 1 <= abs(num-prev_num) <= 3:
                    #print('\tDifference is {} type is {}'.format(abs(num-prev_num), typ))
                    if num < prev_num and typ == -1:
                        #print('\t\tValid Decending')
                        status = True
                    elif num > prev_num and typ == 1:
                        #print('\t\tValid Accending')
                        status = True
                    else:
                        status = False
                        #print('\t----------------Not Valid---------------')
                        break
                else:
                    status = False
                    #print('\t----------------Not Valid---------------')
                    break
            prev_num = num
        #print('REPORT ENDED {}\n\n'.format(ind))
        
        if status:
            safe += 1

    return safe

print(do_challenge())