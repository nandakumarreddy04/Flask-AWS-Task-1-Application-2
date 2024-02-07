Follow this link

https://github.com/avizway1/flask-installation


Below are the steps : 

Downloads % ssh -i "Key pair 18 Jan.pem" ec2-user@ec2-13-233-29-121.ap-south-1.compute.amazonaws.com

sudo su

sudo yum install python3 -y

sudo yum install gcc python3-devel -y

sudo pip3 install virtualenv  (not found pip)

sudo yum install python3-pip

yum install git -y

git clone s    ...

cp -r Flask-App2/* .             …..

cd Flask-App2   ….

python3 -m venv venv

source venv/bin/activate

pip install Flask gunicorn

sudo chmod -R +r /home/ec2-user/Flask-App2    …..

gunicorn -w 1 -b 0.0.0.0:5000 main2:app   ……

 sudo yum install nginx
 
vim /etc/nginx/conf.d/flask-app.conf

Click i   ,  paste it and edit server name     edit Flask-App2  

Click Esc  , type  :wqd

vim /etc/nginx/nginx.conf

Add this server_names_hash_bucket_size 128; under http.   Under  4000

sudo nginx -t

sudo systemctl restart nginx      (error)

 sudo fuser -k 80/tcp
 
sudo fuser -k 443/tcp

sudo service nginx restart

sudo chmod -R +r /home/ec2-user/Flask-App2

nohup gunicorn -w 1 -b 127.0.0.1:5000 app:app > gunicorn.log 2>&1 &         

 change that

nohup gunicorn -w 2 -b 0.0.0.0:5001 main2:app > gunicorn_main2.log 2>&1 &

nohup gunicorn -w 2 -b 0.0.0.0:5000 main1:app > gunicorn_main1.log 2>&1 &


nginx file configuration:



server {
    listen 80;
    server_name ec2-13-232-126-77.ap-south-1.compute.amazonaws.com;
    location /main1 {
            rewrite ^/main1(.*)$ /$1 break;
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /main2 {
            rewrite ^/main2(.*)$ /$1 break;
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    location /static {
        alias /home/ec2-user/Flask-App2/static;
    }
    location /favicon.ico {
        alias /home/ec2-user/Flask-App2/favicon.ico;
    }
error_page 500 502 503 504 /500.html;
    location = /500.html {
        root /home/ec2-user/Flask-App2;
    }
}

