import argparse
import shutil
import os

parser = argparse.ArgumentParser()
parser.add_argument('--variables', nargs='*')
parser.add_argument('--output', nargs=1)
parser.add_argument('--scenepath', nargs=1)
	
args = parser.parse_args()
variables = dict()
for i in xrange(0,len(args.variables),2):
	variables[args.variables[i]] = args.variables[i+1]
output = args.output[0]
scenepath = args.scenepath[0]

if int(variables["value"]) == 1:
	shutil.copyfile(os.path.join(scenepath, "python", "files", "float", "1.g3d"), output)
else:
	shutil.copyfile(os.path.join(scenepath, "python", "files", "float", "2.g3d"), output)