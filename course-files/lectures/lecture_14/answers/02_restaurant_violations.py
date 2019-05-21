# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

# VS Code Hack:
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'data', 'Food_Establishment_Violations.csv')
# End VS Code Hack:

def sort_dictionary(d:dict):
    '''
    Helper function to sort a dictionary
    '''
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )

f = open(file_path, 'r', encoding='utf8', errors='ignore')
violations = {}
for line in f.readlines():
    tokens = line.split(',')
    restaurant = tokens[0]
    if violations.get(restaurant):
        violations[restaurant] += 1
    else:
        violations[restaurant] = 1



for key in sort_dictionary(violations):
    print(key, violations[key])