#Increase the file descriptor limit

exec { 'set new limit':
  command => 'sed -i \'s/^holberton hard nofile .*/holberton hard nofile 90000/g\' /etc/security/limits.conf ; sed -i \'s/^holberton soft nofile .*/holberton soft nofile 90000/g\' /etc/security/limits.conf',
  path    => '/bin/',
}

