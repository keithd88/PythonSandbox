import pandas as pd


# input = pd.read_csv('Day5\\test_input.txt', header = None)

file = open('Day5\\test_input.txt', 'r')
input = file.read()
file.close()

# print(input)

input = input.split('\n\n')
seeds = input[0]
input_maps = input[1:]

# split seeds into items
seeds = seeds.split(': ')
seeds = seeds[1].split()
seeds = list(map(int, seeds)) # convert seeds to integers
min_seed = min(seeds) # find min and max for more efficient calcs
max_seed = max(seeds)

# initialize map dataframe
map_df = pd.DataFrame()

# split maps into lists
all_maps = {}
for index, item in enumerate(input_maps):
    # create new conversion dataframe for each map
    map_conversion = pd.DataFrame({'source': range(0, 100), # change to max_seed+1
                                   'destination': range(0, 100)})

    # separate map name & info
    map_name, map_values = input_maps[index].split(' map:\n') 
    map_values = map_values.split('\n')
    
    print(f'map name: {map_name}, values: {map_values}')

    for values in map_values:
        # extract values from each map
        destination, source, map_range = list(map(int, values.split()))
        print(f'destination: {destination} source: {source}, range: {map_range}')

        new_values = list(range(destination,destination+map_range))

        # assign new values to map
        map_conversion.iloc[source:source+map_range, 1] = new_values

    # now use conversion map to convert seeds to next map
    for index, seed in enumerate(seeds):
        seeds[index] = map_conversion.iloc[seed, 1]
        
    print(seeds)

print(min(seeds))





# for index in all_maps:
#     print(all_maps[index][0])
#     print(all_maps[index][1])

#     map_df[all_maps[index][0]] = all_maps[index][1]
#     print(map_df)
# seed_to_soil = pd.DataFrame(all_maps[0])
# seed_to_soil[['destination','source','range']] = seed_to_soil['seed-to-soil map'].str.split(' ', expand=True)
# soil_to_fertilizer = pd.DataFrame(all_maps[1])
# soil_to_fertilizer[['destination','source','range']] = soil_to_fertilizer['soil-to-fertilizer map'].str.split(' ', expand=True)

# print(seed_to_soil)
# print(soil_to_fertilizer)

# for map_index in all_maps:
#     cur_map = all_maps[map_index]
    
#     print(cur_map)


