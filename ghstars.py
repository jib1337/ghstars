#!/usr/bin/env python3
import urllib.request, json, sys, os

user = 'jib1337'

with urllib.request.urlopen(f'https://api.github.com/users/{user}/starred') as response:
    stardata = json.load(response)

if len(sys.argv) > 1:
    if sys.argv[1].isdigit() and int(sys.argv[1]) <= len(stardata):
        os.system('git clone https://www.github.com/' + stardata[int(sys.argv[1])-1]['full_name'])
        quit()
    else:
        print('Invalid argument.\n')

longest = len(max([repo['full_name'] for repo in stardata], key=len))

for i, repo in enumerate(stardata):
    print(f"{i+1}.\t{repo['full_name']:{longest+1}}", end='')
    if repo['description'] is not None:
        print(f"{repo['description'][:75]}")
    else:
        print()
