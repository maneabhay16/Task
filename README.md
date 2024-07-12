Sum Paid Views by Month and Year
This script processes a CSV file to calculate the sum of paid views for each month and year. It reads the Calendar_Week and Paid_Views columns from the CSV file, sums the paid views for each unique month and year, and handles errors in date parsing and value conversion.

How It Works
Reading the CSV File:

The script opens the CSV file and reads it line by line.
The header row is used to find the indices of the Calendar_Week and Paid_Views columns.
Processing Each Row:

For each row, the script converts the Calendar_Week value to a datetime object.
A (year, month) tuple is created from the date to group the paid views by month and year.
If the date has not been processed before, the Paid_Views value is added to the sum for the corresponding (year, month) in a dictionary.
The date is then marked as processed to avoid duplicate calculations.
Handling Errors:

Errors during date conversion or value conversion are caught and printed, and those rows are skipped.
Summarizing Results:

The script prints the sum of Paid_Views for each month and year after processing all rows.
Usage
Place your CSV file at the desired location on your system.
Update the file_path variable in the script with the path to your CSV file.
Run the script to see the summed paid views by month and year.
