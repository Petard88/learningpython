from datetime import date
from shutil import copyfile

date_backup = date.today()
print(date_backup)

str_date_backup = str(date_backup).replace('-','.')

print(str_date_backup)

path_input = r'/Backup.txt'
path_output = r'C:\Users\Natverkstekniker\Desktop\Petter\GDrive' + '\\' + str_date_backup + ' - Backup.txt'

print(path_output)

copyfile(path_input, path_output)