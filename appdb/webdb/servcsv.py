# Full path and name to your csv file
csv_filepathname="/home/miguel/django/appdb/webdb/servidores.csv"
# Full path to your django project directory
your_djangoproject_home="/home/miguel/django/appdb"
import django 
import sys,os



sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'appdb.settings'
django.setup()


from webdb.models import University
from webdb.models import Professor
import csv

#with open('some.csv', newline='', encoding='utf-8') as f:
#        reader = csv.reader(f)
#            for row in reader:
#                        print(row)

fi =(open(csv_filepathname, encoding='utf-8')) 

dataReader = csv.reader((x.replace('\0', '') for x in fi), delimiter=';')

#fo = data.replace('\x00', '')
#dataReader = csv.reader(fi, delimiter=';')

#print (dataReader)
for row in dataReader:
    if row[0] != 'Id_SERVIDOR_PORTAL' and row[2] == 'PROFESSOR DO MAGISTERIO SUPERIOR': #and row[5] == 'UNIVERSIDADE FEDERAL DE SANTA MARIA' and 'NILZA' in row[1]:
        
        u = University.objects.filter(name=row[5]).first()
        if(u):
            pr = Professor()
            name = row[1]
            fName = name.split(' ', 1)
            pr.firstName = fName[0]
            pr.lastName = fName[1]
            pr.course = ("")
            pr.university = u
            pr.save()


