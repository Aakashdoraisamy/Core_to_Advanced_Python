from itertools import combinations 
def solve(N, K, hubs):
    total_capacity = 0 
    for comb in combinations(hubs, K):
        total_capacity += max(comb) 
    return total_capacity 

custom_input_1 = list(map(str, input().split())) 
N = int(custom_input_1[0]) 
K = int(custom_input_1[1]) 
hubs = list(map(int, input().split())) 
out_ = solve(N, K, hubs) 
print(out_)