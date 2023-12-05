file = open('Day1\\input.txt', 'r')
input = file.read()
file.close()

input_list = input.split('\n')

output_list = []
output_value = 0
for value in input_list:
    if len(value) != 0:
        value = value.replace('one', 'o1e')
        value = value.replace('two', 't2o')
        value = value.replace('three', 't3e')
        value = value.replace('four', 'f4r')
        value = value.replace('five', 'f5e')
        value = value.replace('six', 's6x')
        value = value.replace('seven', 's7n')
        value = value.replace('eight', 'e8t')
        value = value.replace('nine', 'n9e')

        nums = ''.join(filter(str.isdigit, value))
        output = nums[0] + nums[-1]
        output_list.append(output)
        output_value += int(output)

print(output_value)