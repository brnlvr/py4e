file = open("mbox-short.txt")
hour_counts = {}
for line in file:
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(':')[0]
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
for hour in sorted(hour_counts):
    print(hour, hour_counts[hour])
