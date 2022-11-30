print('coding exercise 1')

filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    print(f"{index}-{item}")

print('Coding Exercise 2')

ips = ['100.122.133.105', '100.122.133.111']

# 1. Prompts the user to input an index (e.g, 0 or 1).
# 2. Returns the IP address that has that index

index = int(input('enter index for IP 0 or 1: '))
print(ips[index])
