FROM devopsedu/webapp
ADD website/ /var/www/html/  
RUN apt-get update -y
RUN apt-get install -y libapache2-mod-php7.0 php7.0 apache2
RUN systemctl restart apache2.service
