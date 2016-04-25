import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operation", 
	help="mathematical operation that will be performed", 
	choices=['add', 'subtract', 'multiply', 'divide'])
parser.add_argument("num1", help="the first number", type=int)
parser.add_argument("num2", help="the second number", type=int)
args = parser.parse_args()