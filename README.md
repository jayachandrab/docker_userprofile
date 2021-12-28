# docker_userprofile
After downloading the repo, 
1. Need to have docker isntalled in your machine,
2. need to give 

    docker-compose build
    
The above command  (it will install all the fastapi libraries, uvicrorn server, postgres database and other python libraries)
It will install all the libraries listed in requirements.txt file

2. Then create a file called .env in the main project folder and add the following line

   #DATABASE_URL = postgresql+psycopg2://postgres:postgres@db:5432

3. Need to give 

   docker-compose run web alembic revision --autogenerate -m "First migration" 

The above command, (which places so-called candidate migrations into our new migrations file.)

4. Now lets run the migration command 

   docker-compose run web alembic upgrade head

The above (The alembic upgrade command will run upgrade operations, proceeding from the current database revision)

5. docker-compose up 

The Above command will run the docker image it includes, uvicorn server running fast api and postgress server

6. you can check postgres server by giving below  url in broser 

http://localhost:5050/

you can login with user=pgadmin4@pgadmin.org and password=admin


7. After opening postgress ui In general tab change choose a name for the connection and Connect to database server, and choose password is postgres as well.

8. now you can find the tables Servers > {your-connection-name} >Databases > postgres >Schemas >public>Tables >users

9. To check out fastapi is working, you can open http://localhost:8000/docs in your browser, you can see the list of api end points.


