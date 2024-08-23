#update file descriptor limits
exec { 'first-edit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}


exec { 'second-edit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
  require  => Exec ['first-edit'],
}
