FROM devopsedu/webapp
ADD website/ /var/www/html  
RUN apt-get update
#RUN apt-get install libapache2-mod-php7.0 php7.0 apache2
#RUN systemctl restart apache2.service
EXPOSE 80
FROM devopsedu/webapp
ADD website /var/www/html  
RUN apt-get update
EXPOSE 80
