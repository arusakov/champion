from fabric import task

GIT_REPO = 'https://github.com/afrolovskiy/champion.git '
PROJECT_PATH = '/usr/local/champion'
ENV_DIR = 'env'

@task
def setup(c):
    c.sudo('apt-get update && sudo apt-get install -y {}'.format(' '.join((
        'git', 'python3-pip', 'nginx', 'uwsgi', 'supervisor',
        'virtualenv', 'virtualenvwrapper', 'gunicorn',
    ))))
    c.sudo('mkdir {}'.format(PROJECT_PATH))
    c.sudo('chown ubuntu:ubuntu {}'.format(PROJECT_PATH))
    c.run('git clone {} {}'.format(GIT_REPO, PROJECT_PATH))
    c.run('virtualenv {}/{} --python=python3'.format(PROJECT_PATH,ENV_DIR))
    c.sudo('ln -sf {}/contrib/supervisor.conf /etc/supervisor/conf.d/champion.conf'.format(PROJECT_PATH))
    c.sudo('ln -sf {}/contrib/nginx.conf /etc/nginx/conf.d/champion.conf'.format(PROJECT_PATH))

@task
def deploy(c):
    with c.cd(PROJECT_PATH):
        c.run('git fetch && git reset --hard origin/master')
        c.run('{}/bin/pip3 install -r requirements.txt'.format(ENV_DIR))
        c.run('{}/bin/python3 manage.py migrate'.format(ENV_DIR))
        c.run('{}/bin/python3 manage.py collectstatic --noinput'.format(ENV_DIR))
    c.sudo('supervisorctl reload')
    c.sudo('supervisorctl restart champion')
    c.sudo('systemctl restart nginx')
