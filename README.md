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

        docker-compose up

7. App will start on localhost on port 8000:

        http://localhost:8000/

8. To recieve telegram notification if delivery time expired, just go to below bot on telegram app and just /start it and when web app refreshes it will automaticaly sends notification about outdated orders to users of bot:

        @kanalservicenotificationbot

9. Google sheet to test given edit permision to amkolotov@gmail.com:

        https://docs.google.com/spreadsheets/d/1Z38ZTvYry5glASyyytFY4FcTB_ckiXcMWPN7b9lRZSM/edit#gid=0