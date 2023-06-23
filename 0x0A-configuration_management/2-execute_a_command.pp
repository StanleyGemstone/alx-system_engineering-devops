exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin', '/usr/local/bin'],
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
