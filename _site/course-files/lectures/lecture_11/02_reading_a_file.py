import utilities
f = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')

for line in f:
    print(line)
f.close()