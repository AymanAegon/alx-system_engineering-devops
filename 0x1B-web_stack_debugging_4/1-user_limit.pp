#Increase the file descriptor limit

exec { 'set new hard limit':
  command => 'sed -i \'s/^holberton hard nofile .*/holberton hard nofile 90000/g\' /etc/security/limits.conf',
  path    => '/bin/',
}

-> exec { 'set new soft limit':
  command => 'sed -i \'s/^holberton soft nofile .*/holberton soft nofile 90000/g\' /etc/security/limits.conf',
  path    => '/bin/',
}
