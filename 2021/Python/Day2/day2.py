challenge_input = "input.txt"

depth = 0
horizontal_position = 0

with open(challenge_input, 'r') as file:
    for line in file.readlines():
        current_line = line.strip()
        current_action = current_line.split()[0]
        current_value = int(current_line.split()[1])
        print("Moving {} by {}.".format(current_action, current_value))
        if current_action == "forward":
            horizontal_position += current_value
        elif current_action == "up":
            depth -= current_value
        elif current_action == "down":
            depth += current_value

print("Final depth is {}, final horizontal position is {}".format(depth, horizontal_position))
print("Depth ({}) x Position ({}) = {}".format(depth, horizontal_position, depth * horizontal_position))