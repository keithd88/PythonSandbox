file = open('Day4\\input.txt', 'r')
input = file.read()
file.close()

input = input.split('\n')
total_points = 0

for card in input:
    print(card)

    card_id, card_nums = card.split(': ') # split card id from card info
    card_id = int(card_id.replace('Card ', '')) # get card_id as an int

    my_nums, winning_nums = card_nums.split('| ') # split up each test case
    my_nums = my_nums.split()
    winning_nums = winning_nums.split()

    matches = 0
    for num in winning_nums:
        if num in my_nums:
            matches += 1
    
    card_points = 0
    if matches > 0:
        card_points += 2**(matches-1) # calculate points per card
    
    total_points += card_points

print(total_points)