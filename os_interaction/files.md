# Managing Files with Python

## Reading and Writing Files

Absolute and relative paths.

### Reading Files

```py
file = open("spider.txt")
print(file.readlin())

file.close()
```

Os gives a file descriptor.

Readline reads one line at a time of the file object.

Remember to close files. Can stop other programs from using them, and only a certain number of file descriptors at once.

```py
with open("spider.txt") as file:
	print(file.readline())
```

The `with` keyword allows Python to automatically close after block.

Without it, can use the file in multiple places. Just remember to close it.

### Iterating through Files

```py
with open("spider.txt") as file:
	for line in file:
		print(line.upper())
```

`print` already has a newline:

```py
with open("spider.txt") as file:
	for lin in file:
		print(line.strip().upper())
```

Can read the file into a list with `readline`

```py
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
```

The `lines` is saved after the file is closed.

### Writing Files

```py
with open("novel.txt", "w") as file:
	file.write("It was a dark and stormy night")
```

THe `w` parameter is for write mode. Read-only is the default mode (`r`).
Remember `w` writes over all data. Use the `a` append method.

## Managing Files and Directories

Using the `os` module, to operate on the underlying system without knowing.

```py
import os
os.remove("novel.txt")
```

Use the `remove` module to delete files.

```py
import os
os.rename("first_draft.txt", "finished_masterpiece.txt")
```

`os.path` submodule

```py
os.path.exists("finished_masterpiece.txt")
```

Returns a boolean.

### More File Information

`getsize` function

`getmtime` -> unix timestamp. last modified time.

`isfile()`

```py
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
```

Can use relative or absolute paths.

```py
os.path.abspath("spider.txt")
```

Creates full path starting in the current working directory.

### Directories

`getcwd` -> get current working directory.

```py
print(os.getcwd())
```

`mkdir` -> create a directory

```py
os.mkdir("new_dir")
```

`chdir` -> change directory

```py
os.chdir("new_dir")
```

`rmdir` -> remove empty directories only

`os.listdir` -> returns all files and subdirectories

```py
os.listdir("website")
['images', 'index.html', 'favicon.ico']
```

`os.path.is_dir`

`os.path.join`

```py
import os
os.listdir("website")

# ['images', 'index.html', 'favicon.ico']

dir = "website"
for name in os.listdir(dir):
	fullname = os.path.join(dir, name)
	if os.path.isdir(fullname):
		print(f"{fullname} is a directory")
	else:
		print(f"{fullname} is a file")
# website/images is a directory
# website/index.html is a file
# website/favicon.ico is a file
```

## Reading and Writing CSV Files

Parsing -> analyzing a file's content to correctly structure the data.

### Reading CSV Files

Example

csv.txt

```csv
Sabrina Green, 802-867-5309,System Administrator
Eli Jones, 684-3481127, IT specialist
Melody Daniels, 846-687-7436, Programmer
Charlie Rivera, 698-746-3357, Web Developer
```

Use the `csv` module.

```py
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)

for row in csv_f:
	name, phone, role = row
	print(f"Name: {name}, Phone: {phone}, Role: {role}")

f.close()
```

### Generating CSV

Use a `writer` function.

```py
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]

with open('hosts.csv') as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)
```

Can use `writerow` or `writerows`.

- `cat` command can be used in the terminal to display contents of a file.

### Reading and Writing CSV Files with Dictionaries

It's common for csvs to include the names of columns as the first line:

software.csv

```csv
name, version, status, users
MailTree,5.34,production,324
CalDoor,1.25.1,beta,22
Chatty Chicken,0.34,alpha,4
```

Can use `DictReader`.
Then can use column names instead of rows.

```py
with open('software.csv') as software:
	reader = csv.DictReader(software)
	for row in reader:
		print(f"{row["name"]} has {row["users"]} users")
```

Order of the fields doesn't matter.

`DictWriter`

```py
users = [
	{
		"name": "Sol Mansi",
		"username": "solm",
		"department": "IT Infrastructure",
	},
	{
		"name": "Lio Nelson",
		"username": "lion",
		"department": "User Experience Research",
	},
	{
		"name": "Charlie Grey",
		"username": "greyc",
		"department": "Development",
	},
]

keys = ["name", "username", "department"]

with open('by_departement.csv', 'w') as by_department:
	writer = csv.DictWriter(by_department, fieldnames=keys)
	writer.writeheader()
	writer.writerows(users)

```

### More Reading

[Reading and Writing Csv Files in Python - Real Python](https://realpython.com/python-csv/)

## Lab

```py
!/usr/bin/env python3

import csv

def main():
    pass

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_list = []

    with open(csv_file_location) as file:
        reader = csv.DictReader(file, dialect='empDialect')
        #reader = csv.DictReader(file)
        for row in reader:
            employee_list.append(dict(row))

    return employee_list


def process_data(employee_list):

    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):

    with open(report_file, 'w+') as file:
        for k in sorted(dictionary):
            file.write(f'{k}: {dictionary[k]} \n')

employee_list = read_employees('/home/student/data/employees.csv')

dictionary = process_data(employee_list)

write_report(dictionary, '/home/student/test_report.txt')
```
