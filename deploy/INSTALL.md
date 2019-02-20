sudo apt-get update

sudo apt-get install -y git python3-pip nginx uwsgi supervisor virtualenv virtualenvwrapper gunicorn

cd /usr/local/

sudo git clone https://github.com/afrolovskiy/champion.git 

sudo chown ubuntu:ubuntu -R champion

virtualenv /usr/local/champion/env --python=python3 

/usr/local/champion/env/bin/pip3 install -r /usr/local/champion/requirements.txt

cd /usr/local/champion

source env/bin/activate

env/bin/python3 manage.py migrate

env/bin/python3 manage.py collectstatic --noinput

sudo ln -sf /usr/local/champion/deploy/supervisor.conf /etc/supervisor/conf.d/champion.conf

sudo ln -sf /usr/local/champion/deploy/nginx.conf /etc/nginx/conf.d/champion.conf

sudo supervisorctl reload

sudo supervisorctl restart champion

sudo /etc/init.d/nginx restart


---


git fetch

git reset --hard origin/master

