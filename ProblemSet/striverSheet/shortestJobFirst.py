jobs = eval(input("Enter the jobs: "))
jobs.sort()
waiting_time =0
total_waiting_time = 0
for job in jobs:
    waiting_time+=total_waiting_time
    total_waiting_time+=job
print("The average waiting time is:", waiting_time/len(jobs))