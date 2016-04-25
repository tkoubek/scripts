#! /usr/bin/env python

"""
BASH: for file in `ls *.feature`; do grep "Feature:" $file | sed 's/Feature: //g'; donesed 's/\<word\>//g'

"""

maindir = '/home/gekko/dev/wicked-testsuite/features'


import glob

filelist = '/home/gekko/dev/wicked-testsuite/features/*.feature'
listing = sorted(glob.glob(filelist))
keyword = "Feature: "

feature = []
for filename in listing :
    for line in open(filename):
        if keyword in line:
            print line
            feature.append(line)

print(len(feature))
print(feature[3])


def main():
     """Runs program and handles command line options"""

if __name__ == '__main__':
    main()