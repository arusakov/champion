# champion

virtualenv -p python3.6 env
source env/bin/activate
pip install -r requirements.txt

## deploy

fab --hosts=champion --ssh-config ~/.ssh/config deploy
