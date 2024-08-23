#maximum number of file descriptors Nginx can open

#'fix-nginx' modifies the Nginx configuration file

exec { 'fix-nginx':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path     => '/usr/local/bin/:/usr/bin'
  notify   => Service['nginx']
}

#'nginx-restart' restarts the Nginx service

exec { 'nginx-restart':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['fix-nginx'],
}
