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

exec { 'add_custom_header':
  provider => shell,
  command  =>
    "sed -i '/^\tserver_name _;/a \\t\\tadd_header X-Served-By \$(hostname);' /etc/nginx/sites-available/default",
  require  => Package['nginx'],
}

exec { 'restart_server':
  provider => shell,
  command  => 'sudo service nginx restart',
}
