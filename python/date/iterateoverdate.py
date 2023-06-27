from datetime import datetime
from dateutil.relativedelta import relativedelta


start_date = datetime.strptime("31/12/2022","%d/%m/%Y")
end_date = datetime.strptime("1/1/2021","%d/%m/%Y")
current_date = start_date
steps = 40
count = 0
while current_date >= end_date:
	if count == steps:
		break
	count+=1
	print(current_date)
	current_date -= relativedelta(months=1)
