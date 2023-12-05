file = open('Day2\\input.txt', 'r')
input = file.read()
file.close()

input_list = input.split('\n')

output_num = 0

for game in input_list:
    print(game)

    game_id, game_info = game.split(': ') # split game id from game info
    game_id = int(game_id.replace('Game ', '')) # get game_id as an int

    game_info = game_info.split('; ') # split up each test case

    red = 0
    green = 0
    blue = 0

    for test_case in game_info:
        cube_num = test_case.split(', ')
        # print(test_case)

        for cubes in cube_num:
            if 'red' in cubes:
                new_red = int(''.join(filter(str.isdigit, cubes)))
                if new_red > red:
                    red = new_red
            elif 'green' in cubes:
                new_green = int(''.join(filter(str.isdigit, cubes)))
                if new_green > green:
                    green = new_green
            elif 'blue' in cubes:
                new_blue = int(''.join(filter(str.isdigit, cubes)))
                if new_blue > blue:
                    blue = new_blue

    print(f'Game {game_id} requires minimum {red} red, {green} green, and {blue} blue cubes')
    output_num += red*green*blue



print(output_num)