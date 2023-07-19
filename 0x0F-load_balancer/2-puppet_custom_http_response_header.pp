#Automates the whole configuration done in task 0

exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sed -i "40i\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
} 
