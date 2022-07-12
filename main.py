from mainfuncs import *

def main():
	ip_add = extract_ip()
	cont = True
	while cont:
		try:
			choice = int(input("Would you like to do a quick sweep or extensive sweep? Type 1 for quick or 2 for extensive\n(Note: An extensive sweep will take longer, but be more accurate, especially for devices that take a while to respond):"))
			if choice == 1:
				quicktest(ip_add)
			elif choice == 2:
				extensivetest(ip_add)
			else:
				print("Invalid response")
				continue
		except ValueError:
			print("Invalid response")
		else:
			cont = False

if __name__ == '__main__':
	main()
