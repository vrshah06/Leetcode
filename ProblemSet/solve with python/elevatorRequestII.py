n = int(input("Number of floors: "))
requests = eval(input("Enter a list of requests: "))
start_floor = int(input("Enter the starting floor: "))
penalty = 0
total_time = 0
current_floor = start_floor
for request in requests:
    if request == start_floor:
        penalty+=0
    else:
        total_time += abs(request - current_floor)
        current_floor = request
print(penalty)

