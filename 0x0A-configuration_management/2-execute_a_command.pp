#2. Execute a command
#Using Puppet, create a manifest that kills a process named killmenow.
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
