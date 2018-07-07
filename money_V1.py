import os
import pyexcel
from copy import copy

days_l = [day for day in open(
    os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Money.txt'), 'r').read().replace('\n', '').split(';') if day]

# split each day into each position and divide date and transactions
temp_0 = [[date_, trans.split(',')] for day in days_l for date_, trans in [day.split(':')]]

# create a pair for each position (date, transaction)
temp_1 = [[day[0], trans] for day in temp_0 for trans in day[1]]

# split each position into (date, sum, description, is_cash)
temp_2 = [[day[0], sum_, desc[:-1].title(), int(desc[-1])] for day in temp_1 for sum_, desc in [day[1].split(' ')]]

# Convert list into proper output format
cashed_block = []
for block in temp_2:
    block.insert(1, 'Expense') if float(block[1]) < 0 else block.insert(1, 'Income')
    block.insert(3, '-')
    block.insert(5, '-'), block.insert(5, 'Me')
    block[0] = block[0].replace('.', '/')
    block[2] = block[2].replace('.', ',')
# alternative flow for cashed position, creates mirror position with income to match cashed expense position
if block[4] == 'Cashed':
    block[3] = 'Cashed'
    cashed_block = copy(block)
    cashed_block[2], cashed_block[1], cashed_block[7] = str(abs(int(block[2]))), 'Income', 1

temp_2.insert(-1, cashed_block) if cashed_block else None
temp_2.sort()
pyexcel.save_as(array=temp_2, dest_file_name=os.path.join(os.environ['USERPROFILE'], 'Desktop', 'money_out.tsv'))