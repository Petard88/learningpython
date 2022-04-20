import usb.core
import shutil
from datetime import date
import win32api

date_backup = date.today()
str_date_backup = str(date_backup).replace('-','.')

path_input1 = r'c:\Users\Natverkstekniker\PycharmProjects'
path_input2 = r'c:\Users\Natverkstekniker\Documents\Övningar'
path_input3 = r'c:\Users\Natverkstekniker\Desktop\Petter\Inlamningsuppgifter'
path_output = r'F:' + '\\' + str_date_backup + ' auto-backup folder'

dev = usb.core.find(idVendor=0x090C, idProduct=0x1000)
pathlist = [path_input1, path_input2, path_input3]
stickaninfo = win32api.GetVolumeInformation("F:\\")
accepted_id = ['STICKAN', 571776173, 255, 131590, 'exFAT']
given_id = []

if dev:
    for stinf in stickaninfo:
        if stinf in accepted_id:
            given_id.append(stinf)
        else:
            print("no soup for you")
if given_id == accepted_id:
    for pathing in pathlist:
        shutil.copytree(pathing, path_output, dirs_exist_ok=True)
