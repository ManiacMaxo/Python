from math import sqrt

def prime_generator():
	count = 3
	while True:
		prime = True
		for num in range(2, int(sqrt(count) + 1)):
			if count % num == 0: 
				prime = False
				break
		if prime:
			print(count)
		count += 1


if __name__ == "__main__":
    print('starting')
    prime_generator()