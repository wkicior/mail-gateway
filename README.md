# mail-gateway
E-mail gateway for sending forecast notifications

#first copy and edit settings file
cp com/github/wkicior/mailgateway/settings_sample.py com/github/wkicior/mailgateway/settings.py
vim com/github/wkicior/mailgateway/settings.py

#build
docker build -t wkicior/mail-gateway .

#run
docker run --privileged=true -it -v /home/disorder/praca/helyeah/mail-gateway:/app:rw --rm -p 9998:80 wkicior/mail-gateway


