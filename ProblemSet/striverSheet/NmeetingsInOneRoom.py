start = eval(input("Enter start times: "))
end = eval(input("Enter end times: "))
meetings = []
for i in range(len(start)):
    meetings.append((start[i], end[i], i + 1))
meetings.sort(key=lambda x: x[1])
print(meetings)
result = []
prev_end = -1
for meeting in meetings:
    if meeting[0] >= prev_end:
        result.append(meeting[2])
        prev_end = meeting[1]
print(result)