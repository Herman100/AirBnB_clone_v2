# puppet file static content deployment
exec { 'server update':
  command => '/usr/bin/env apt-get -y update',
}
-> exec {'ensure x':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec {'directory release/test':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'Creates directories':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'custom test':
  command => '/usr/bin/env echo "simple content" | sudo tee /data/web_static/releases/test/index.html',
}
-> exec {'Sym link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> exec {'ownership and group':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
-> exec {'configure x':
  command => '/usr/bin/env sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'restart x':
  command => '/usr/bin/env service nginx restart',
}
