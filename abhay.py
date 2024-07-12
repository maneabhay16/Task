import csv
from datetime import datetime

def sum_paid_views_by_month_and_year(file_path):
    sums_by_month_and_year = {}  
    processed_dates = set()  

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  

        for row in reader:
            try:
                
                calendar_week_index = header.index('Calendar_Week')
                paid_views_index = header.index('Paid_Views')
                
                
                calendar_week = datetime.strptime(row[calendar_week_index], '%m/%d/%Y')
            except ValueError as e:
                print(f"Skipping row due to error: {e}")
                continue
            year_month = (calendar_week.year, calendar_week.month)
            
            if calendar_week not in processed_dates:
                print(f"Including date: {calendar_week}")
                try:
                    paid_views = int(row[paid_views_index])
                    
                    if year_month not in sums_by_month_and_year:
                        sums_by_month_and_year[year_month] = 0
                    
                    sums_by_month_and_year[year_month] += paid_views
                    
                    processed_dates.add(calendar_week)
                except ValueError as e:
                    print(f"Skipping row due to error: {e}")
    
    return sums_by_month_and_year

file_path = r'C:\Users\Abhay\OneDrive\Desktop\task\csvv.csv'
result = sum_paid_views_by_month_and_year(file_path)
for (year, month), sum_paid_views in result.items():
    print(f"The sum of Paid Views for {month}/{year} is: {sum_paid_views}")
