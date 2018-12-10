USE securities_master;

CREATE TABLE data_vendor (
id int NOT NULL AUTO_INCREMENT,
name varchar(64) NOT NULL,
website_url varchar(255) NULL,
support_email varchar(255) NULL,
created_date datetime NOT NULL,
last_updated_date datetime NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

insert into data_vendor (id,name,website_url,support_email,created_date,last_updated_date) value (1,'Alpha Vantage', null,null,sysdate(),sysdate())