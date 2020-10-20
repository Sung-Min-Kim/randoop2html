import json, copy, sys
from json2html import *

with open(sys.argv[1]) as f:
    data = json.load(f)

with open(sys.argv[2]) as f:
    data2 = json.load(f)

# Helping Methods
def remove_line_info(locs):
    if type(locs) == list:
        for i in range(len(locs)):
            loc = locs[i].rsplit(":", 1)[0] + ")"
            locs[i] = loc
    elif type(locs) == str:
        locs = locs.rsplit(":", 1)[0] + ")"

    return locs

def remove_description(exception):
    exception = exception.split(":", 1)
    return exception[0]

# exception type(+description), full stack, + line number
def method1(case):
    equal = False
    for i in data['descriptions']:
        if(i['exception']==case['exception']):
            loc1 = i['location']
            loc2 = case['location']
            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(+description), full stack, - line number
def method2(case):
    equal = False
    for i in data['descriptions']:
        if(i['exception']==case['exception']):
            loc1 = remove_line_info(i['location'])
            loc2 = remove_line_info(case['location'])

            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(-description), full stack, + line number
def method3(case):
    equal = False
    for i in data['descriptions']:
        exception1 = remove_description(i['exception'][0])
        exception2 = remove_description(case['exception'][0])
        if(exception1 == exception2):
            loc1 = i['location']
            loc2 = case['location']
            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(-description), full stack, - line number

def method4(case):
    equal = False
    for i in data['descriptions']:
        exception1 = remove_description(i['exception'][0])
        exception2 = remove_description(case['exception'][0])
        if(exception1 == exception2):
            loc1 = remove_line_info(i['location'])
            loc2 = remove_line_info(case['location'])

            if loc1 == loc2:
                equal = True
            else:
                break

    return equal


# exception type(+description), top-most, + line number
def method5(case):
    equal = False
    for i in data['descriptions']:
        if(i['exception']==case['exception']):
            loc1 = i['location'][0]
            loc2 = case['location'][0]

            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(-description), top-most, + line number
def method6(case):
    equal = False
    for i in data['descriptions']:
        exception1 = remove_description(i['exception'][0])
        exception2 = remove_description(case['exception'][0])
        if(exception1 == exception2):
            loc1 = i['location'][0]
            loc2 = case['location'][0]

            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(+description), top-most, -line number
def method7(case):
    equal = False
    for i in data['descriptions']:
        if(i['exception']==case['exception']):
            loc1 = remove_line_info(i['location'][0])
            loc2 = remove_line_info(case['location'][0])

            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(-description), top-most, -line number
def method8(case):
    equal = False
    for i in data['descriptions']:
        exception1 = remove_description(i['exception'][0])
        exception2 = remove_description(case['exception'][0])
        if(exception1 == exception2):
            loc1 = remove_line_info(i['location'][0])
            loc2 = remove_line_info(case['location'][0])

            if loc1 == loc2:
                equal = True
            else:
                break

    return equal

# exception type(+description), no stack
def method9(case):
    equal = False
    for i in data['descriptions']:
        if(i['exception']==case['exception']):
            equal = True

    return equal

# exception type(-description), no stack
def method10(case):
    equal = False
    for i in data['descriptions']:
        exception1 = remove_description(i['exception'][0])
        exception2 = remove_description(case['exception'][0])
        if(exception1 == exception2):
            equal = True

    return equal
    
# Save the result
cnt = 0
data3 = []
method_key = 'method' + sys.argv[3]
method_dict = {
    'method1': method1,
    'method2': method2,
    'method3': method3,
    'method4': method4,
    'method5': method5,
    'method6': method6,
    'method7': method7,
    'method8': method8,
    'method9': method9,
    'method10': method10
}

for i in data2['descriptions']:
    if not method_dict[method_key](i):
        cnt+=1
        data3.append(copy.deepcopy(i))


trial_num = sys.argv[4]
bug_num = sys.argv[5]


filename = "bug"+bug_num+"-"+"try"+trial_num+"-"+method_key+".json"
with open(filename, 'w') as outfile:
    json.dump(data3, outfile, indent=4)
# html = json2html.convert(json = data3)
# print(cnt)
# print(html)

