filename = input("Enter file name: ")
count = 0
total = 0
file = open(filename)
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        value = float(line[line.find(':') + 1:].strip())
        count = count + 1
        total = total + value
average = total / count
print("Average spam confidence:", average)
