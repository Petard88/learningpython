import usb
import shutil
from datetime import date
import sys, os, fcntl, struct

date_backup = date.today()
str_date_backup = str(date_backup).replace('-','.')

path_input1 = r'c:\Users\Natverkstekniker\PycharmProjects'
path_input2 = r'c:\Users\Natverkstekniker\Documents\Övningar'
path_input3 = r'c:\Users\Natverkstekniker\Desktop\Petter\Inlamningsuppgifter'
path_output = r'F:' + '\\' + str_date_backup + ' auto-backup folder'

dev = usb.core.find(idVendor=0x090C, idProduct=0x1000)
seri =


input_list = [path_input1, path_input2, path_input3]

if dev:
    for path in input_list:
        shutil.copytree(path, path_output, dirs_exist_ok=True)
