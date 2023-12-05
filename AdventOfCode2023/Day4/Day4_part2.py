import pandas as pd

total_copies = pd.read_csv('Day4\\input.txt', header=None)
total_copies['copies'] = 1
total_copies['matches'] = 0

# print(total_copies)


for card in total_copies[0]:
    card_id, card_nums = card.split(': ') # split card id from card info
    card_id = int(card_id.replace('Card ', '')) # get card_id as an int

    my_nums, winning_nums = card_nums.split('| ') # split up each test case
    my_nums = my_nums.split()
    winning_nums = winning_nums.split()

    matches = 0
    for num in winning_nums:
        if num in my_nums:
            matches += 1 

    total_copies.iloc[card_id-1, 2] = matches # record # of matches per card


for card_id in range(len(total_copies)):
    copies = total_copies.iloc[card_id, 1]
    matches = total_copies.iloc[card_id, 2]
    
    if matches != 0:
        total_copies.iloc[card_id+1:card_id+1+matches, 1] += (1 * copies) # multiply new copies added by number of copies you have

print(total_copies['copies'].sum())