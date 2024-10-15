input = str(input())

input = input.replace('pp', '$')
input = input.replace('p', '')
input = input.replace('$', 'p')

print(input)