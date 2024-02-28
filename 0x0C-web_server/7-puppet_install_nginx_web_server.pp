# Configures a new Ubuntu machine to respect following requirements

package { 'nginx':
  ensure => 'present',
}

exec { 'root_page':
  provider => shell,
  command  => 'sudo echo Hello World! > /var/www/html/index.html',
}

exec { 'redirect':
  provider => shell,
  command  =>
    'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/oluwaseundasilva.hashnode.dev\/;\\n\\t}/" /etc/nginx/sites-available/default'
  ,
}

exec { 'restart_server':
  provider => shell,
  command  => 'sudo service nginx restart',
}
