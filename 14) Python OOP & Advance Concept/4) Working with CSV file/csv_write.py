import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL)       #csv.writer python le diyeko inbuilt class ho

    employee_writer.writerow(['emp_name', 'dept', 'birth date'])        #.writerow python ko inbuilt class ho
                                                                          # line  6,7,8,9 sabbai  with open vitra lekhna parxa... identation ko khyal gar
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica meyers', 'IT', 'March'])
    employee_writer.writerow(['Hey Hi Hello', 'Good', 'Bye'])
