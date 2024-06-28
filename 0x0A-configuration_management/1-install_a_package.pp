#Using Puppet, install flask from pip3.i
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
