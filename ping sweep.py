from os import system
from platform import system as ostype

def quicktest() -> None:
    for i in range(1, 254):
        system(f"ping -w 250 -c 2 10.0.0.{i} >> results.txt")

def extensivetest() -> None:
    for i in range(1, 254):
        system(f"ping -c 3 10.0.0.{i} >> results.txt")

def main():
    cont = True
    while cont:
        try:
            choice = int(input("Would you like to do a quick sweep or extensive sweep? Type 1 for quick or 2 for extensive\n(Note: An extensive sweep will take longer, but be more accurate, especially for devices that take a while to respond):"))
            if choice == 1:
                quicktest()
            elif choice == 2:
                extensivetest()
            else:
                print("Invalid response")
                continue
        except ValueError:
            print("Invalid response")
        else:
            cont = False

if __name__ == '__main__':
    main()
```python
from os import system
from platform import system as ostype

def quicktest() -> None:
    for i in range(1, 254):
        system(f"ping -w 250 -c 2 10.0.0.{i} >> results.txt")

def extensivetest() -> None:
    for i in range(1, 254):
        system(f"ping -c 3 10.0.0.{i} >> results.txt")

def main():
    cont = True
    while cont:
        try:
            choice = int(input("Would you like to do a quick sweep or extensive sweep? Type 1 for quick or 2 for extensive\n(Note: An extensive sweep will take longer, but be more accurate, especially for devices that take a while to respond):"))
            if choice == 1:
                quicktest()
            elif choice == 2:
                extensivetest()
            else:
                print("Invalid response")
                continue
        except ValueError:
            print("Invalid response")
        else:
            cont = False

if __name__ == '__main__':
    main()
