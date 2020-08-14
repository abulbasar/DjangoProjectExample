mkdir -p /tmp/deployment && cd /tmp/deployment
git clone git@github.com:abulbasar/DjangoProjectExample.git
cd DjangoProjectExample
git checkout dev
# add a step to install virtualenv if necessary
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd MyDjangoProject
export GUNICORN_CMD_ARGS="--bind=0.0.0.0 --workers=10"
gunicorn MyDjangoProject.wsgi


