#Sync 
###application for collecting and storing user data for Department of Biomedical Informatics at Harvard Med School 
## Set up Environment
```
dnf install python-virtualenv
mkdir syncapp && cd $_
mkdir syncenv
virtualenv syncenv
```
##Get and Run Application
```
git clone https://github.com/jcirni/sync.git
source syncenv/bin/activate
pip install django==1.9.3
python ./sync/mysite/manage.py runserver
firefox http://localhost:8000/sync/
```
