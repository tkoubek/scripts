import argparse

parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('list',
                    #action='store_true',
                    help='list flag')

args = parser.parse_args()

if args.list :
    print("List!")
else:
    print("Nothing...")