def divide(a, b):
	c = []
	try:
		for i in range(0, 6):
			c.append(a[i] // b)
		return c
	except ZeroDivisionError as e:
		print("Exception!!!!")
		print(e)
	except IndexError as e:
		print("Exception!!!!")
		print(e)
	except Exception as e:
		print("Exception!!!!")
		print(e)
	finally:
		print("Finally Block")


if __name__ == "__main__":
	# Driver Code
	try:
		n = int(input("Enter N: "))
	except ValueError:
		print("Invalid number")
		raise

	x = []
	print("Enter List Elements:")
	for i in range(n):
		try:
			x.append(int(input()))
		except ValueError:
			print("Invalid element, expected integer")
			raise

	try:
		y = int(input("Enter b: "))
	except ValueError:
		print("Invalid divisor")
		raise

	c = divide(x, y)
	print(c)
	