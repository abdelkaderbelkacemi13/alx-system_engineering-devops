#update file descriptor limits

exec { 'first-edit':
  provider => shell,
  'sed -i -e "s/nofile 5/nofile 99999/" \
	    -e "s/nofile 4/nofile 99999/" \
	    /etc/security/limits.conf',
}
