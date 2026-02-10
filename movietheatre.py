import math

for ad in range (0,201,25):
    additional = 2 * round(math.sqrt(ad))
    attendees = 20 + additional
    revenue = attendees * 10
    costs = 200 + ad
    profit = revenue - costs
    print(ad, profit)

ad = 0
while ad <= 200:
    additional = 2 * round(math.sqrt(ad))
    attendees = 20 + additional
    revenue = attendees * 10
    costs = 200 + ad
    profit = revenue - costs
    print(ad, profit)
    ad += 25
