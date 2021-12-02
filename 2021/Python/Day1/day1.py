challenge_input = "input.txt"

last_depth = 0
depth_increases = 0

with open(challenge_input, 'r') as file:
    for line in file.readlines():
        current_depth = line.strip()
        if last_depth == 0:
            last_depth = current_depth
            print("Starting the dive to {}".format(last_depth))
            depth_increases += 1
            continue
        else:
            if current_depth > last_depth:
                print("Diving from {} to {}".format(last_depth, current_depth))
                last_depth = current_depth
                depth_increases += 1
                continue
            elif last_depth > current_depth:
                print("Surfacing from {} to {}".format(last_depth, current_depth))
                last_depth = current_depth
                continue

print("Total depth increases = {}".format(depth_increases))