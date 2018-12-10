 CREATE DATABASE securities_master;
 USE securities_master;

 CREATE USER 'sec_user'@'localhost' IDENTIFIED BY 'password';
 GRANT ALL PRIVILEGES ON securities_master.* TO 'sec_user'@'localhost';
  FLUSH PRIVILEGES;