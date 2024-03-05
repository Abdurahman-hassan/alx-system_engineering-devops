# This Puppet manifest installs the Nginx web server and adds a new HTTP header to the default site configuration file.

exec { 'update packages':
  provider => 'shell',
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
  ensure   => 'present',
  provider => apt,
}

file_line { 'add new HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => "add_header X-Served-By \"${hostname}\";"
}

exec { 'restart_server':
  provider => shell,
  command  => 'sudo service nginx restart',
}
