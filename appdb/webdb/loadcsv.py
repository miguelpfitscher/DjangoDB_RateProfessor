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

#with open('some.csv', newline='', encoding='utf-8') as f:
#        reader = csv.reader(f)
#            for row in reader:
#                        print(row)


dataReader = csv.reader(open(csv_filepathname, encoding='utf-8'), delimiter=';', quotechar='"')


for row in dataReader:
    if row[0] == '2011': # Ignore the header row, import everything else
        uni = University()
        uni.name = row[2].encode('utf-8')
        uni.sigla = row[3].encode('utf-8')
        #print (row[2].encode('utf-8'))
        #print (row[3].encode('utf-8'))
        uni.save()

