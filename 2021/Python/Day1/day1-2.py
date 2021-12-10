from collections import deque

challenge_input = "input.txt"

last_sum = 0
current_sum = 0
count = 0

with open(challenge_input, 'r') as file:

    for line in file.readlines():
        current_depth = line.strip()

        if last_sum == 0:
            dq = deque([current_depth])
            last_sum = 1

        else:
            if len(dq) < 3:
                dq.appendleft(current_depth)
            elif len(dq) == 3:
                current_sum = 0
                for q in dq:
                    current_sum += int(q)
                dq.pop()
                dq.appendleft(current_depth)
                if current_sum > last_sum:
                    count += 1
                last_sum = current_sum

print("The number of times the three measurement window increased compared to the last one is {}".format(count))