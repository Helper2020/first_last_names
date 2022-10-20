import csv

'''
Script to scrape first and last names from two files, file of first names and file of last names. 
Then combine the first and last names.
'''

# Lets start with first names.
first_names_set = set()

with open('first_names.txt', 'r', encoding="utf-8") as f:
    # the first_name file has over 1000 names. We will keep it at 1000
    first_name_count = 0
    limit = 1000

    for first_name in f:
        first_names_set.add(first_name.strip())
        first_name_count += 1

        if first_name_count == limit:
            break


# Now for the last names. We're working with a csv file
# file has exactly 1000 last names
last_names_set = set()

with open('most-common-name_2Fsurnames.csv', mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    last_name_count = -1

    for row in csv_reader:
        if last_name_count == -1:
            last_name_count += 1
            continue
        
         # Last name is all caps let's change that
        last_name = row[1].strip().capitalize()
        last_names_set.add(last_name)
        
        last_name_count += 1
    

# Checking if name appears in both sets. If so change
num_common_names = len(first_names_set.intersection(last_names_set))
print("Any names in both sets? " + str(num_common_names))
# Here we get names in both sets
common_names = first_names_set.intersection(last_names_set)
# take common names out of first set
first_names_set_clean = first_names_set.difference(common_names)
# take common names out of second set
last_names_set_clean = last_names_set.difference(common_names)

# lets add 24 to each set to make it an even 900
# first name set
count = 0
while count != 24:
    first_names_set_clean.add(common_names.pop())
    count += 1
# last name set
count = 0
while count != 24:
    last_names_set_clean.add(common_names.pop())
    count += 1

# Final check for common names in both set
num_common_names = len(first_names_set_clean.intersection(last_names_set_clean))
print("Any names in both sets? " + str(num_common_names))

# combine names
rowid = [idx for idx in range(1, 901)]
full_names = zip(rowid, first_names_set_clean, last_names_set_clean)

with open('full_names900.csv', mode="w", newline='') as full_name_file:
    name_write = csv.writer(full_name_file, delimiter=',')

    fields = ['RowID','First_Name', 'Last_Name']

    name_write.writerow(fields) 
    name_write.writerows(full_names)







