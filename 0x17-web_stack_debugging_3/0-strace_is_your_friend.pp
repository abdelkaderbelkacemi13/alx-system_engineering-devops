# 0. Strace is your friend task

exec {'fix a wordpress website':
  provider => shell,
  command  => 'sudo sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
