from datetime import datetime
from dateutil.relativedelta import relativedelta

current_date = datetime.now()
#current_date = datetime(2023,2, 28)
endOfMonth = current_date + relativedelta(day=31)
if current_date == endOfMonth:
	print("date is end of month")
print(endOfMonth)
