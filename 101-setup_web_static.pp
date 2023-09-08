# sets up web servers for deployment of web_static
exec { 'update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure  => present,
  require => Exec['update'],
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

file_line { 'server_name':
  path  => '/etc/nginx/sites-available/default',
  line  => '\tserver_name _;',
  match => '^(\s*)server_name.*$',
}

file_line { 'location':
  path  => '/etc/nginx/sites-available/default',
  line  => '\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n',
  after => '^(\s*)server_name.*$',
}

service { 'nginx':
  ensure => running,
  enable => true,
}
