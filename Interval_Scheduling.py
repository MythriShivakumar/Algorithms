def interval_scheduling_coving(n, u, v, intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: (interval[1], interval[0])) 
    sorted_intervals_for_schedule = sorted(intervals, key=lambda interval: interval[0])
    current_schedule = u
    maximum = 0
    minimum  = 0
    last_end_time = 0
    index = 0
    for interval_start, interval_end in sorted_intervals:
        if interval_start >= last_end_time:
            maximum += 1
            last_end_time = interval_end
    while current_schedule < v:
        best_next_end = current_schedule
        while index < n and sorted_intervals_for_schedule[index][0] <= current_schedule:
            best_next_end = max(best_next_end, sorted_intervals_for_schedule[index][1])
            index += 1
        if best_next_end == current_schedule:
            return maximum, "no"
        current_schedule = best_next_end
        minimum += 1
    return maximum, minimum



def read_input():
    n, u, v = map(int, input().split())
    intervals = []
    for _ in range(n):
        s, f = map(int, input().split())
        intervals.append((s, f))
    return n, u, v, intervals


if __name__ == "__main__":
    n, u, v, intervals = read_input()
    maximum, minimum = interval_scheduling_coving(n, u, v, intervals)
    print(maximum)
    print(minimum)
