#configure SSH client to use private keY ~/ssh/holberton adn refuse to authenticate usign pswrd
include stdlib

file_line { 'Use private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Refuse password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
