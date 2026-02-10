for hours in range(1, 9):
    fee = 5.00 + 2.50 * hours
    if fee < 10:
        fee = 10.0
    elif fee > 20:
        fee = 20.0
    print(hours, fee)

hours = 1
while hours <= 8:
    fee = 5.00 + 2.50 * hours
    if fee < 10:
        fee = 10.0
    elif fee > 20:
        fee = 20.0
    print(hours, fee)
    hours += 1
