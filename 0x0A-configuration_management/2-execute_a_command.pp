# kills the process'killmenow'

exec {'pkill -f killmenow':
  path => '/usr/bin/:/bin/',
} 
