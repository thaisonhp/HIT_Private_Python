import math

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def read():
    with open('/Users/luongthaison/Documents/năm 2023 -  SV năm 2/Python/Python-HIT-Private/week-6/btvn/input.txt', 'r') as file:
        my_list = [i for i in file.read().split() if is_integer(i) or is_float(i)]
    return list(map(float, my_list))

def output():
    with open('/Users/luongthaison/Documents/năm 2023 -  SV năm 2/Python/Python-HIT-Private/week-6/btvn/output.txt', 'w') as output_file:
        x1, y1, x2, y2 = read()
        AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        formatted_distance_AB = "{:.2f}".format(AB)
        output_file.write(f"A({x1},{y1}) B({x2},{y2}) AB = {formatted_distance_AB}")


output()