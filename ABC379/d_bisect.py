import sys
import bisect

Q = int(sys.stdin.readline())
plant_times = []
total_time = 0
harvested = 0
outputs = []

for _ in range(Q):
    query = sys.stdin.readline().strip().split()
    if query[0] == '1':
        plant_times.append(total_time)

    elif query[0] == '2':
        T = int(query[1])
        total_time += T
        
    elif query[0] == '3':
        H = int(query[1])
        target_time = total_time - H
        idx = bisect.bisect_right(plant_times, target_time, harvested)
        num_harvested = idx - harvested
        outputs.append(str(num_harvested))
        harvested = idx

print('\n'.join(outputs))
