file = open('Day2\\input.txt', 'r')
input = file.read()
file.close()

input_list = input.split('\n')

max_red = 12
max_green = 13
max_blue = 14

output_num = 0

for game in input_list:
    game_id, game_info = game.split(': ') # split game id from game info
    game_id = int(game_id.replace('Game ', '')) # get game_id as an int
    print(game)
    game_info = game_info.split('; ') # split up each test case
    for test_case in game_info:
        cube_num = test_case.split(', ')
        print(cube_num)
        for cubes in cube_num:
            if 'red' in cubes:
                red = int(''.join(filter(str.isdigit, cubes)))
                if red > max_red:
                    flag = False
            elif 'green' in cubes:
                green = int(''.join(filter(str.isdigit, cubes)))
                if green > max_green:
                    flag = False
            elif 'blue' in cubes:
                blue = int(''.join(filter(str.isdigit, cubes)))
                if blue > max_blue:
                    flag = False
    break        
    
    

    
print(output_num)