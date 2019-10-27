A = input()

def main():
	chars = list(A)
	if len(chars) > 1:
		print(''.join(chars[0:-1]))
		return
	elif len(chars) == 1 and chars[0] != 'a':
		print('a')
		return
	else:
		print('-1')

main()

# N, X = map(int, input().split(" "))
# x = list(map(int, input().split(" ")))

# answers = []

# def calc(n):
# 	if n == 0:
# 		return 1 + X + 4 + X
# 	else:
# 		cost1 = answers[n - 1] + n + X + 4 * n + X
# 		cost2 = answers[n - 1] + X

# def main():
# 	for i in range(0, N):
# 		answers.append(calc(i))
# 	print(answers[-1])

# main()

# t = int(input())

# def sub(a, b, c, d):
# 	values = [a]
# 	i = a
# 	while (True):
# 		i = i % b if i > b else i - b
# 		if i < 0:
# 			return 'No'
# 		if i <= c:
# 			i += d
# 		if i in values:
# 			return 'Yes'
# 		values.append(i)
# 	return 'No'

# def main():
# 	for i in range(0, t):
# 		a, b, c, d = map(int, input().split(' '))
# 		print(sub(a, b, c, d))

# main()
