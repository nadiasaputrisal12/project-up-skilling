#math 
import math

print(math.sqrt(25))
print(math.pi)

# random
import random

print(random.randint(1,100))
print(random.choice(['merah','biru','hijau']))

# datetime
import datetime

sekarang = datetime.datetime.now()
print(sekarang)
print(sekarang.strftime('%d-%m-%Y'))

# os
import os 

direktori_sekarang = os.getcwd()
print(direktori_sekarang)
os.mkdir('folder_baru')