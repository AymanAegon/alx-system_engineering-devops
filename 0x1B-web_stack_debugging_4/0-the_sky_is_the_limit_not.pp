#fix nginx webserver

exec { 'Set new limit':
  command => 'sed -i \'s/^ULIMIT=.*/ULIMIT="-n 4096"/g\' /etc/default/nginx',
  path    => '/bin/',
}

-> exec { 'restart nginx server':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
