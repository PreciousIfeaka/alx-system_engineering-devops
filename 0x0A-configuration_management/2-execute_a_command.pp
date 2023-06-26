# This manifest kills the killmenow process

exec {'kill_killmenow':
  command     => 'pkill killmenow',
  refreshonly => 'true',
  path        => '/usr/bin',
}
