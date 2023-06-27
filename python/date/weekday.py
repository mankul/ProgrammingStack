from datetime import date

d = date(2023,1,1)

if d.weekday() == 0: # 0 is for monday
	print("its a monday")

if d.weekday() == 1: # 0 is for tuesday
	print("its a tuesday")

if d.weekday() == 2: # 0 is for wednesday
	print("its a wednesday")

if d.weekday() == 3: # 0 is for thursday
	print("its a thursday")

if d.weekday() == 4: # 0 is for friday
	print("its a friday")

if d.weekday() == 5: # 0 is for saturday
	print("its a saturday")

if d.weekday() == 6: # 0 is for sunday
	print("its a sunday")

else:
	print("not a weekday or a weekend")
