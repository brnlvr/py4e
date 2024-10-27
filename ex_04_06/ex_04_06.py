def computepay(hours, rate):
    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * (rate * 1.5)
        total = regular + overtime
    else:
        total = hours * rate
    return total
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = computepay(hours, rate)
print("Pay", pay)
