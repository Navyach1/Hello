n = int(input("Amount: "))
if n in range(1000,2000):
	print("Discount is 10%")
	Discount = (10/100) * n
	print(Discount)
	AmountToBePaid = n - Discount
	print(f"TotalAmount is {AmountToBePaid}")
elif n in range(2000,3000):
	print("Discount is 20%")
	Discount = (20/100) * n
	print(Discount)
	AmountToBePaid = n - Discount
	print(f"TotalAmount is {AmountToBePaid}")
elif n in range(3000,5000):
	print("Discount is 30%")
	Discount = (30/100) * n
	print(Discount)
	AmountToBePaid = n - Discount
	print(f"TotalAmount is {AmountToBePaid}")
elif n > 5000:
	print("Discount is 40%")
	Discount = (40/100) * n
	print(Discount)
	AmountToBePaid = n - Discount
	print(f"TotalAmount is {AmountToBePaid}")
else:
	print("Amount is lessthan 1000, so there is null Discount")