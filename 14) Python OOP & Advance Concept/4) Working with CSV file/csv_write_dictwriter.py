#dictionary content lai csv format file ma laijane tarika
import csv

with open('employee_file2.csv', mode='w') as csv_file:         #employee_file2.csv vanni file kholera dictionary ko content lai write garxa tesma 
    keys =['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=keys)   #csv file column header haru chai fieldnames ma halxa with help of keys

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    
 


                                                                       