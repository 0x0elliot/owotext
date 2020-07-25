import pyperclip

while True:
	var=input("Enter your string: ")
	var=var.replace("l","w")
	var=var.replace("r","w")
	var=var.replace('o','ow')
	print(var)
	pyperclip.copy(var)
