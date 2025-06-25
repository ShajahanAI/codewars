# https://www.codewars.com/kata/56d46b8fda159582e100001b/train/python

# Passed

def travel(total_time, run_time, rest_time, speed):
    distance_covered = 0
    while total_time > 0:
        remaining_run_time = min(run_time, total_time)
        distance_covered += speed * remaining_run_time
        total_time -= run_time + rest_time

    return distance_covered

output = travel(35869784, 90, 100, 5)
print(output)