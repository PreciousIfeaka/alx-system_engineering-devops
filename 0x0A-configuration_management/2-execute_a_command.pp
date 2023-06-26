# This manifest kills the killmenow process

exec {'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
