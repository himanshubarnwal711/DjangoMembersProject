So this is a very simple project for my group members.
You just need to clone this project.

git clone https://github.com/himanshubarnwal711/DjangoMembersProject.git

Either be in ubuntu or linux.

Ensure that python3.10.12 and pip3 - 22.0.2 are installed with the below commands

sudo apt update

sudo apt install -y python3.10.12

sudo apt install python3 python3-pip

pip3 install --upgrade pip==22.0.2

Then install Django

python3 -m pip install Django==5.1.7

django-admin --version 
#5.1.7



Run these commands
python3 manage.py makemigrations artworks
python manage.py migrate

Run this server at 127.0.0.1:8000/
python3 manage.py runserver



Go to cd Testproject/

Directly run the Dockerfile:-
cd TestProject/
docker build -t django-artworks .
docker run -p 8000:8000 django-artworks

Or you can directly run docker public image:-
docker run -p 8000:8000 rrai2229/django-artworks:latest
