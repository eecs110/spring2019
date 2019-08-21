# At the command line: 
# pip install wikipedia

import wikipedia

term = input('What do you want to search for? ')
results = wikipedia.search(term)

print(results)
print(*results, sep='\n')

page = wikipedia.page('Northwestern_University')
print(page.content)