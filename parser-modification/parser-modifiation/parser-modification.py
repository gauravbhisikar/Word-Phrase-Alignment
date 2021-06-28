import os
import re
import sys
import ast


with open(sys.argv[1],'r') as f:
    cont = f.readlines()

new_cont = re.sub(r'\([^\s]+', '[', cont[0])
new_cont1 = re.sub(r'\)', ']', new_cont)
new_cont2 = re.sub(r'\] ', '],', new_cont1)
new_cont3 = re.sub(r' ', '', new_cont2)
new_cont4 = re.sub(r'\[([^\[\]]+)\]', r'["\1"]', new_cont3)




#my_parse = ast.literal_eval(new_cont4)

print('my_list = '+ new_cont4)
