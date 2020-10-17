FROM devopsedu/webapp
ADD website/ /var/www/html/  
RUN apt-get update -y
RUN apt-get install -y libapache2-mod-php7.0 php7.0 apache2
RUN service apache2 start
#RUN sleep 30; /etc/init.d/apache2 reload
