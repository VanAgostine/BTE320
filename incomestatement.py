sales = float(input("Enter sales: $"))
tax_rate = float(input("Enter tax rate %: "))

cogs = sales * 0.40
gp = sales - cogs
taxes = gp * (tax_rate / 100)
ni = gp - taxes

print(f"Sales ${sales:.0f}")
print(f"COGS ${cogs:.0f}")
print(f"GP ${gp:.0f}")
print(f"Taxes ${taxes:.0f}")
print(f"NI ${ni:.0f}")

