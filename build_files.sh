pip3 install --upgrade pip
pip3 install -r requirements.txt

python3 manage.py collectstatic --noinput

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
