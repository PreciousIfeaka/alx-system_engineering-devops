# This puppet script installs and configures nginx on the remote server

exec { 'nginx configuration':
  provider => shell,
  command  => 'apt-get -y update; apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.nginx-debian.html; sed -i "/listen 80 default_server/a rewrite ^/tredirect_me http://www.youtube.com/watch?v=JCxGxK3GZiA permanent;" /etc/nginx/sites-available/default'
}
