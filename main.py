# Naive bayes algorithm implementation in python
import csv
import copy
from sys import argv

def main():
	matrix = readcsv(argv[1])
	prob = posterior(matrix, argv[2], argv[3:])

# Determine P(class | c1, c2, .. cn)
def posterior(matrix, targetclass, conditions):
	# find target class column index
	tcol = matrix[0].index(targetclass)
	# find condition column indices
	ccol = [matrix[0].index(cond.split(":")[0]) for cond in conditions]
	# find condtion values respectivly
	cval = [cond.split(":")[1] for cond in conditions]
	# construct needed frequency tables
	ftables = [freqtable(matrix, cn, tcol) for cn in ccol]
	# construct needed likehood tables, in same order as ftables
	ltables = [likehoodtable(ftable) for ftable in ftables]
	# possible classes
	classes = list(set(column(matrix[1:], matrix[0].index(targetclass))))
	# outcomes for per possible class, in same order as classes
	outcomes = [1] * len(classes)
	# for each possible class, determine the P(class| c1 c2, .. cn)
	for cl, i in zip(classes, range(0, len(classes))):
		# for each condition provided
		for cn in range(0, len(ccol)):
			# get relevant likehood table
			liketable = ltables[cn]
			# find P(condition|class)
			plike = liketable[column(liketable, 0).index(cval[cn])][liketable[0].index(cl)]
			# determine P(condition)
			pcond = len([v for v in column(matrix[1:], ccol[cn]) if v == cval[cn]])/len(matrix)
			# multiply P(condition|class) and P(condition)
			outcomes[i]*= plike*pcond

	for cl, i in zip(classes, range(0, len(classes))):
		pstr = "P(" + cl + "|"
		for condval in cval:
			pstr += condval + ","
		pstr = pstr[:-1] + ") = " + str(outcomes[i])
		print(pstr)

	print("The classified class is '" + classes[outcomes.index(max(outcomes))] + "'")

# Construct P(condition | class) table 
def likehoodtable(ftable):
	ctable = copy.deepcopy(ftable)
	# rename table name as P(condition|class)
	ctable[0][0] = "P" + ctable[0][0][1:]
	# for each column starting from 1
	for c in range(1, len(ctable[0])):
		# column sum - sum of frequences of the current column 
		csum = sum(column(ftable[1:], c))
		# for each row starting from 1
		for r in range(1, len(ctable)):
			ctable[r][c] = ctable[r][c] / csum
	return ctable

# Construct frequency table
def freqtable(matrix, ccol, tcol):
	# matrix headerless
	matrixhl = matrix[1:]
	# table name
	tn = "f(" + matrix[0][ccol] + "|" + matrix[0][tcol] + ")" 
	# header
	ftable = [[tn] + list(set(column(matrixhl, tcol)))]
	# for each unique condition
	for ucond in set(column(matrixhl, ccol)):
		row = [ucond]
		# for each header(class) value
		for cval in ftable[0][1:]:
			# construct row with their corresponding frequency values
			row += [len([r for r in matrixhl if r[ccol] == ucond and r[tcol] == cval])]
		ftable.append(row)

	return ftable

# Slice column from matrix
def column(matrix, c):
	return [row[c] for row in matrix]

# Read matrix from csv file
def readcsv(filename):
	matrix = []
	with open(filename, "r") as csvfile:
		for line in csvfile:
			matrix.append(line.strip().split(","))

	return matrix

# Pretty print matrix
# For debug purposes
def pmatrix(matrix):
	for row in matrix:
		print(row)
	print()	# newline

if __name__ == '__main__':
	main()
