# Ensure the SSH client config directory exists
file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Ensure the SSH client config file exists
file { '/home/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
}

# Configure SSH to use the private key and refuse password authentication
file_line { 'Declare identity file':
  path => '/home/ubuntu/.ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  replace => true,
}
