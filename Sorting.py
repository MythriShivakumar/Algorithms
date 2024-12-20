def ascending_sort(cities):
    if len(cities) <= 1:
        return cities
    pivot = cities[len(cities) // 2]
    left = []
    middle = []
    right = []
    for city in cities:
        if (city[1], city[0]) < (pivot[1], pivot[0]):
            left.append(city)
        elif (city[1], city[0]) == (pivot[1], pivot[0]):
            middle.append(city)
        else:
            right.append(city)
    sorted_cities = ascending_sort(left) + middle + ascending_sort(right)
    return sorted_cities


def read_input():
    cities = []
    while True:
        city_input = input().strip()
        if not city_input:
            break
        city_info = city_input.split()
        city_index, population = int(city_info[0]), int(city_info[1])
        cities.append((city_index, population))

    return cities


if __name__ == "__main__":
    cities = read_input()
    sorted_cities = ascending_sort(cities)
    for city in sorted_cities:
        print(city[0], city[1])
