#! /usr/bin/env python

"""
BASH:  find . -name "*.feature" -type f -exec grep "Scenario: " {} \; | grep -v '#' | wc -l

"""

maindir = '/home/gekko/dev/wicked-testsuite/features'

import glob
import re

filelist = '/home/gekko/dev/wicked-testsuite/features/*.feature'
listing = sorted(glob.glob(filelist))
keyword = "Scenario: "

# scenario = []
scenarios = {}
count = 0
for filename in listing:
    for line in open(filename):
        # Building a dictionary with scenario name and number (As shown in Cucumber Reports)
        if (keyword in line and re.search(r'#', line) is None):

            key = format((000 + 1 + count), '03d')
            value = line.strip()
            scenarios[key] = value
            #print(scenarios[key])
            #print(key.strip())
            print(key.title().strip() + " ==> " + scenarios[key])
            count +=1       #count + 1


#print("papa:", scenarios.get(054))

#def get_range(scenarios, begin, end):
#    result = {}
#    for (key,value) in scenarios.iteritems():
#        if key >= begin and key <= end:
#            result[key] = value
#    return result


#get_range(scenarios,'001','020')

#import itertools
#def get_range(dictionary, begin, end):
#  return dict(itertools.islice(dictionary.iteritems(), begin, end+1))

#print get_range(scenarios,11,40)

def main():
    """Runs program and handles command line options"""


if __name__ == '__main__':
    main()