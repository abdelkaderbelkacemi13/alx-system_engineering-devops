#update file descriptor limits
exec { 'first-edit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 99999/" /etc/security/limits.conf',
}


exec { 'second-edit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 99999/" /etc/security/limits.conf',
  require  => Exec ['first-edit'],
}
