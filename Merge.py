def merge_sort_cities_by_population(cities):
    if len(cities) <= 1:
        return cities
    mid = len(cities) // 2
    left_cities = merge_sort_cities_by_population(cities[:mid])
    right_cities = merge_sort_cities_by_population(cities[mid:])
    return merge_sorted_cities(left_cities, right_cities)


def merge_sorted_cities(left_cities, right_cities):
    merged_cities = []
    i, j = 0, 0
    while i < len(left_cities) and j < len(right_cities):
        if left_cities[i][1] <= right_cities[j][1]:
            merged_cities.append(left_cities[i])
            i += 1
        else:
            merged_cities.append(right_cities[j])
            j += 1
    merged_cities.extend(left_cities[i:])
    merged_cities.extend(right_cities[j:])
    return merged_cities


def solve(n, k, city_populations):
    # ----------------------------- #
    sorted_cities = merge_sort_cities_by_population(city_populations)
    # ----------------------------- #
    return {
        'index': sorted_cities[k-1][0], # you should set this field to the index of kth the least populated city.
        'population': sorted_cities[k-1][1] # you should set this field to the population of kth the least populated city.
    }


def read_input():
    n, k = map(int, input().split())
    city_populations = []
    for _ in range(n):
        idx, population = map(int, input().split())
        city_populations.append((idx, population))
    return n, k, city_populations


if __name__ == "__main__":
    n, k, city_populations = read_input()
    res = solve(n, k, city_populations)
    print(res['index'], res['population'])
