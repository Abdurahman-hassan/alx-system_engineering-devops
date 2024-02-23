# Create a file with the content "I love Puppet" in /tmp/school with the following permissions: 0744, owned by www-data:www-data.
file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
