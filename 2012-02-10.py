# Ahad H. Shabbir
# Programming Challange #1 With Bonus - 2012-02-10
# Python 3.7

import re, sys

removeWhiteSpace = lambda s: re.sub(r'\s+', r'', s)

name = input('Enter your name: ').strip()
sAge = input('Enter your age: ').strip()
username = input('Enter your username: ').strip()

nameInvalidator = re.compile(r'[^A-z]')
usernameInvalidator = re.compile(r'[^\w]')
ageInvalidator = re.compile(r'[^\d]')

# Use regex invalidators to check for appropriate charecters.
if nameInvalidator.search(removeWhiteSpace(name)):
     sys.exit(f'Error: Name \'{name}\' is invalid.' 
          + ' It must only be english and whitespace charecters.')

if ageInvalidator.search(sAge):
     sys.exit(f'Age: \'{sAge}\' is invalid. It must only be digits 0-9.')
else:
     age = int(sAge)

if usernameInvalidator.search(username):
     sys.exit(f'Username: \'{username}\' is invalid.'
          + 'It must be only alphanumeric charecters')

# Print to screen.
print(f'Your name is {name}, you are {age} years old,',
     f'and your username is {username}.')

# Sync information to FILENAME, print output of FILENAME.
FILENAME = '2012-02-10_userdata.csv'
choice = ''
try:
     dataFile = open(FILENAME, 'x')
     dataFile = open(dataFile.name, 'a+')
except FileExistsError:
     while not (choice == 'y' or choice == 'n'):
          choice = removeWhiteSpace(input(f'File \'{FILENAME}\' exists,' 
               + ' continue? (y/n): '))
     if choice == 'y':
          print('Ok, appending to the end of the file...')
          dataFile = open(FILENAME, 'a+') 
     elif choice ==  'n':
          exit(0)
     else:
          raise Exception('Implementation Error!')

dataFile.write(','.join((name,str(age),username)))
dataFile.write('\n')
dataFile.seek(0)
print(dataFile.read())
     
