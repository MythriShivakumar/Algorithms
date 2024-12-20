def lifo_cache_miss(k, requests):
    cache = []
    misses = 0
    for request in requests:
        if request not in cache:
            misses += 1
            if len(cache) == k:
                cache.pop() 
            cache.append(request) 
    return misses

def ff_cache_miss(k, requests):
    cache = []
    misses = 0
    future_requests = {page: [] for page in requests}
    for i, request in enumerate(requests):
        future_requests[request].append(i)
    for request in requests:
        if request not in cache:
            misses += 1
            if len(cache) == k:
                page_to_remove = None
                furthest_index = -1
                for page in cache:
                    if future_requests[page]:
                        index = future_requests[page][0] 
                        if index > furthest_index:
                            furthest_index = index
                            page_to_remove = page
                    else:
                        page_to_remove = page
                        break
                cache.remove(page_to_remove)
            cache.append(request)
        future_requests[request].pop(0)
    return misses

def LIFO_FF(k, n, m, requests):
    lifo_miss_count = lifo_cache_miss(k, requests)
    ff_miss_count = ff_cache_miss(k, requests)
    sum = lifo_miss_count + ff_miss_count
    dif = lifo_miss_count - ff_miss_count
    return sum, dif


def read_input():
    k, n, m = map(int, input().split())
    requests = []
    for _ in range(m):
        request = int(input())
        requests.append(request)
    return k, n, m, requests


if __name__ == "__main__":
    k, n, m, requests = read_input()
    sum, dif = LIFO_FF(k, n, m, requests)
    print(sum, dif)
