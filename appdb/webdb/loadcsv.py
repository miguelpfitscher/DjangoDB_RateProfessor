# Full path and name to your csv file
csv_filepathname="/home/miguel/django/appdb/webdb/uni.csv"
# Full path to your django project directory
your_djangoproject_home="/home/miguel/django/appdb"
import django 
import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'appdb.settings'
django.setup()
from webdb.models import University

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

for row in dataReader:
    if row[0] == '2011': # Ignore the header row, import everything else
        uni = University()
        #uni.name = row[3]
        #uni.sigla = row[4]
        print (row[3])
        #uni.statecode = row[2]
        #uni.statename = row[3]
        uni.save()

