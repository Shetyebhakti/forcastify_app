import csv
import random
from datetime import datetime, timedelta

def generate_sample_data_with_dates(size):
    start_date = datetime(2020, 1, 1)  # Start date for the range of dates
    end_date = datetime(2023, 12, 31)  # End date for the range of dates
    
    # Generate random dates within the specified range
    dates = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(size)]
    
    # Generate corresponding sample values
    values = [random.randint(1, 1000) for _ in range(size)]
    
    # Combine dates and values into a list of tuples
    sample_data = list(zip(dates, values))
    
    return sample_data

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['date', 'value'])
        for row in data:
            csv_writer.writerow([row[0].strftime('%m-%d-%Y'), row[1]])  # Update the date format here

sample_data_with_dates_100 = generate_sample_data_with_dates(100)

write_to_csv('random_datasets.csv', sample_data_with_dates_100)

print("CSV file 'random_datasets.csv' has been created.")
