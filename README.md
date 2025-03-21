# System control orders

> Description:\
Project for control orders in cafe
from web-ui 
---

> PDF resume: \
https://drive.google.com/file/d/1jpY_ejq3rC-s9Suvt70Nmub3CqnrlsyO/view?usp=sharing
---

> View video demo: \
https://youtu.be/iUiB6RLdtHc
----

> Demo screen\
![alt text](/demo_screen/im1.png)
![alt text](/demo_screen/im2.png)
![alt text](/demo_screen/im3.png)
---

> Install and lauch
>```bash
># copy repo from git
>git clone https://github.com/YuranIgnatenko/system_control_orders.git
>
># change directory
>cd system_control_orders
>
># create virtual enviroment
>python -m venv venv_cafe
>
># start virtual env.
>source venv_cafe/bin/activate
>
># install packages python from file .txt
>pip install -r requirements.txt
>
># create sql-requests from models.py
>python manage.py makemigrations
>
># using migrations - write tables in storage
>python manage.py migrate
>
># create your user-admin (fill fields in terminal)
>python manage.py createsuperuser
>
># starting server
>python manage.py runserver
>
># url for launch web-ui
>echo "Move to link: [http://127.0.0.1:8000/view_orders]"
>```
