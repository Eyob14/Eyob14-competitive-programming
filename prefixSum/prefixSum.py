# Python Program to find
# prefix sum of 2d array
R = 4
C = 5

# calculating new array
def prefixSum2D(matrix) :
	global C, R
	prefix_sum = [[0 for x in range(C)]
			for y in range(R)]
	prefix_sum[0][0] = matrix[0][0]

	# Filling first row
	# and first column
	for i in range(1, C) :
		prefix_sum[0][i] = (prefix_sum[0][i - 1] +
					matrix[0][i])
	for i in range(0, R) :
		prefix_sum[i][0] = (prefix_sum[i - 1][0] +
					matrix[i][0])

	# updating the values in
	# the cells as per the
	# general formula
	for i in range(1, R) :
		for j in range(1, C) :

			# values in the cells of
			# new array are updated
			prefix_sum[i][j] = (prefix_sum[i - 1][j] +
						prefix_sum[i][j - 1] -
						prefix_sum[i - 1][j - 1] +
						matrix[i][j])

	# displaying the values
	# of the new array
	for i in range(0, R) :
		for j in range(0, C) :
			print (prefix_sum[i][j],
				end = " ")
		print ()

# Driver Code
a = [
    [ 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1 ],
	[ 1, 1, 1, 1, 1 ]
    ]

prefixSum2D(a)

# This code is contributed by
# Manish Shaw(manishshaw1)
