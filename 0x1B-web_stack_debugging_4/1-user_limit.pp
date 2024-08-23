#update file descriptor limits
exec {'first-edit':
  command => 'sudo sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}


exec {'second-edit':
  command => 'sudo sed -i "/holberton soft/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
