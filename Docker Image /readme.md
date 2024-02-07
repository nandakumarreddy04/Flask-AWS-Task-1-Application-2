Follow video

https://www.youtube.com/watch?v=0eMU23VyzR8

python3 -m venv venv

source venv/bin/activate


1. docker build -t myfirstimage:latest .     ( before this Rancher desktop has to run )
2. docker container run -d -p  2000:5000 myfirstimage:latest   

( -d is detached even after ctrl+C , it will work in background )
( 2000 is which it will work  and exposed port is not important)
(5000 is which we are running in index.py)

3. docker container ls
4. docker container stop 076f ( object image )


Remarks -  Flask version is important as said by our Manager  ( but latest version won't work )
