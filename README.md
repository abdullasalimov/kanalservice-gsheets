# Kanalservice

## Build and run the container

1. Install Docker

2. Download this repository
    ```
    git clone https://github.com/abdullasalimov/kanalservice-gsheets.git
    ```
3. Go to directory
    ```
    cd kanalservice-gsheets
    ```

6. On the command line, within this directory, do this to build the image and start the container:

        docker-compose up --build -d

6. After successfully build docker container get container id of db not web container:

        docker ps

7. Migrate postgres database with inputing container id:

        docker exec -it {container_id} python manage.py migrate

9. To use admin panel create super user with below command:

        docker exec -it {container_id} python manage.py createsuperuser

10. To recieve telegram notification if delivery time expired, just go to below bot on telegram app and just /start it and when web app refreshes it will automaticaly sends notification about outdated orders to users of bot:

        @kanalservicenotificationbot
