import csv
from statistics import median


def extract_columns(csv_file_path, new_csv_file_path):
    # Open the CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        extracted_data = []
        for row in csv_reader:
            extracted_row = row[:4]
            a = row[11]
            extracted_row.append(str(a))
            extracted_data.append(extracted_row)
    with open(new_csv_file_path, 'w', newline='', encoding='utf-8') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerows(extracted_data)


def calculate(keywords: str = '', restricted: tuple = (0, 15), size: float = 0.0, whether_CH: bool = True,
              whether_up: bool = True, print_or_not: bool = False) -> None:
    with open('new_pimento3.csv', 'r', encoding='utf-8') as c:
        reader = csv.reader(c)
        lst = []
        lst2 = []
        s = {}
        for row in reader:
            keywords = keywords.lower()
            if keywords in str(row[4]).lower():
                if whether_CH:
                    # calculate crown height
                    if whether_up:
                        # include upper
                        if 'A' in str(row[3]) or "L" in str(row[3]):
                            if row[1] != '':
                                p = position(str(row[3]).lower())
                                if p >= restricted[0] and p <= restricted[1]:
                                    if float(row[1]) >= size:
                                        lst.append(float(row[1]))
                                        lst2.append(position(str(row[3]).lower()))
                                        if row[4] in s:
                                            s[row[4]] += 1
                                        else:
                                            s[row[4]] = 1
                                        if print_or_not:
                                            print(
                                                f'{position(str(row[3]).lower())}, {str(row[3])}, {str(row[4])}, '
                                                f'crown height is {float(row[1])}')
                    else:
                        if not ('A' in str(row[3]) or "L" in str(row[3])):
                            if row[1] != '':
                                p = position(str(row[3]).lower())
                                if p >= restricted[0] and p <= restricted[1]:
                                    if float(row[1]) >= size:
                                        lst.append(float(row[1]))
                                        lst2.append(position(str(row[3]).lower()))
                                        if row[4] in s:
                                            s[row[4]] += 1
                                        else:
                                            s[row[4]] = 1
                                        if print_or_not:
                                            print(
                                                f'{position(str(row[3]).lower())}, {str(row[3])}, {str(row[4])}, '
                                                f'crown height is {float(row[1])} ')
                else:
                    # measure crown width
                    if whether_up:
                        # not include upper
                        if 'A' in str(row[3]) or "L" in str(row[3]):
                            if row[2] != '':
                                p = position(str(row[3]).lower())
                                if p >= restricted[0] and p <= restricted[1]:
                                    if float(row[2]) >= size:
                                        lst.append(float(row[2]))
                                        lst2.append(position(str(row[3]).lower()))
                                        if row[4] in s:
                                            s[row[4]] += 1
                                        else:
                                            s[row[4]] = 1
                                        if print_or_not:
                                            print(
                                                f'{position(str(row[3]).lower())}, {str(row[3])}, {str(row[4])}, corwn '
                                                f'width is {float(row[2])}')
                    else:
                        if not ('A' in str(row[3]) or "L" in str(row[3])):
                            if row[2] != '':
                                p = position(str(row[3]).lower())
                                if p >= restricted[0] and p <= restricted[1]:
                                    if float(row[2]) >= size:
                                        lst.append(float(row[2]))
                                        lst2.append(position(str(row[3]).lower()))
                                        if row[4] in s:
                                            s[row[4]] += 1
                                        else:
                                            s[row[4]] = 1
                                        if print_or_not:
                                            print(
                                                f'{position(str(row[3]).lower())}, {str(row[3])}, {str(row[4])}, '
                                                f'crown width is {float(row[2])}')
        k = ''
        if whether_up:
            k += 'upper teeth'
        else:
            k += 'lower teeth'
        g = ''
        if whether_CH:
            g += 'CH'
        else:
            g += 'CW'
        x = ''
        y = ''
        if whether_up:
            if restricted[0] <= 3:
                x += 'A' + str(restricted[0])
            else:
                x += 'L' + str(restricted[0] - 3)
            if restricted[1] <= 3:
                y += 'A' + str(restricted[1])
            else:
                y += 'L' + str(restricted[1] - 3)
        else:
            if restricted[0] <= 3:
                x += 'a' + str(restricted[0])
            else:
                x += 'l' + str(restricted[0] - 3)
            if restricted[1] <= 3:
                y += 'a' + str(restricted[1])
            else:
                y += 'l' + str(restricted[1] - 3)
        me_pos = median(lst2)
        median_pos = ''
        if whether_up:
            if me_pos > 3:
                median_pos += 'L' + str(me_pos - 3)
            else:
                median_pos += 'A' + str(me_pos)
        else:
            if me_pos > 3:
                median_pos += 'l' + str(me_pos - 3)
            else:
                median_pos += 'a' + str(me_pos)
        if size > 0.0:
            print(f'The {g} of {k} are restricted to be larger than {size}')
        if restricted != (0, 15):
            print(f'The tooth position is restricted to within the range of {(x, y)}, inclusively.')
        print(f'The data is composed of: {s} \nPosition are {k}, and measures {g}.')
        print(
            f'The mean {g}: {sum(lst) / len(lst)}, median {g}:{median(lst)} ,mean position:{sum(lst2) / len(lst2)}, '
            f'median position:'
            f'{median_pos}, n = {len(lst)}')


def position(pos: str) -> float | int:
    # print(pos)
    a = int(pos[1])
    b = int(pos[4])
    if str(pos[0]) == 'l':
        a += 3
    if str(pos[3]) == 'l':
        b += 3
    if len(pos) == 12:
        c = int(pos[8])
        d = int(pos[11])
        if str(pos[7]) == 'l':
            c += 3
        if str(pos[10]) == 'l':
            d += 3
            # print(pos, a, b, c, d)
        return (a + b + c + d) / 4
    # print(pos, a, b)
    return (a + b) / 2


def interact():
    keyword = input('What is the keyword?')
    keyword = keyword.lower()
    restricted_s = int(input('How do you want to restrict the position? Start position? Enter a number'))
    restricted_end = int(input('How do you want to restrict the position? End position? Enter a number.'))
    restricted = (restricted_s, restricted_end)
    size = float(input('Enter a size you wanna restrict(float)'))
    whether_CH = input('Do you want to measure crown height? yes|no').lower()
    if whether_CH == 'yes':
        whether_CH = True
    else:
        whether_CH = False
    whether_up = input('Do you want to measure upper teeth? yes|no\n').lower()
    if whether_up == 'yes':
        whether_up = True
    else:
        whether_up = False
    calculate(keyword, restricted, size, whether_CH, whether_up, False)


def tl(position: str, cw: float | int, whether_A: bool):
    with open('new_correction.csv', 'r', encoding='utf-8') as c:
        reader = csv.reader(c)
        if whether_A:

            for row in reader:
                # print(row[1])
                if 'adult' in row[0]:
                    # print('reach')
                    if row[1] == position:
                        scw = cw / float(row[2])
                        if position[0] == 'a' or position[0] == 'l':
                            new_scw = scw / 852.4 * 1093.7
                            tl = 9.18 * (new_scw * 2) ** 0.97
                            print(f'Base on your input, the upper scw for this individual is {new_scw}mm\nCalculate '
                                  f'TL is {tl / 100}m\n')
                            print(f'correction factor is {float(row[2])}, standardized correction factor for upper '
                                  f'jaw: {float(row[2]) / 1093.7 * 852.4}')
                            return
                        tl = 9.18 * (scw * 2) ** 0.97
                        print(f'Base on your input, the upper scw for this individual is {scw}mm\nCalculate '
                              f'TL is {tl / 100}m\n')
                        print(f'correction factor is {float(row[2])}')

        else:
            for row in reader:
                if 'j' in row[0]:
                    if row[1] == position:
                        scw = cw / float(row[2])
                        if position[0] == 'a' or position[0] == 'l':
                            new_scw = scw / (612.2 + 611.6) * (790.9 + 783.5)
                            tl = 9.18 * (new_scw * 2) ** 0.97
                            print(
                                f'Base on your input, the upper scw for this individual is {new_scw}mm\nCalculate TL is {tl / 100}m\n')
                            print(f'correction factor is {float(row[2])}, standardized correction factor for upper '
                                  f'jaw: {float(row[2]) / (790.9 + 783.5) * (612.2 + 611.6)}')
                            return
                        tl = 9.18 * (scw * 2) ** 0.97
                        print(f'Base on your input, the upper scw for this individual is {scw}mm\nCalculate '
                              f'TL is {tl / 100}m\n')
                        print(f'correction factor is {float(row[2])}')
