def sum_substr(num):
	mod = 10 ** 9 + 7

	s = 0
	f = 1
	for i in range(len(num)-1, -1, -1):
		s = (s + int(num[i]) * f * (i + 1)) % mod
		f = (f * 10 + 1) % mod

	return s

def main():
	number = input().strip()
	print(sum_substr(number))

if __name__ == "__main__":
	main()