You can use the eval built-in. For example, this would work if each dictionary entry is on a different line:

dicts_from_file = []
with open('myfile.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line)) 