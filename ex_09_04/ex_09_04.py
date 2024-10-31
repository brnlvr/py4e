filename = open(input("Enter file name: "))
counts = {}
for line in filename:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
max_email = None
max_count = 0
for email, count in counts.items():
    if count > max_count:
        max_email = email
        max_count = count
print(max_email, max_count)
