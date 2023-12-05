file = open('Day1\\input.txt', 'r')
input = file.read()
file.close()

input_list = input.split('\n')

output_list = []
output_value = 0
for value in input_list:
    if len(value) != 0:
        nums = ''.join(filter(str.isdigit, value))
        output = nums[0] + nums[-1]
        output_list.append(output)
        output_value += int(output)

print(output_value)