# create schema thss collate utf8_general_ci;

use thss;

create table alembic_version
(
	version_num varchar(32) not null
		primary key
);

create table post
(
	id int auto_increment
		primary key,
	user_id int null,
	title varchar(255) null,
	content varchar(255) null,
	last_replied_user_id int null,
	last_replied_time datetime null,
	created datetime null,
	updated datetime null
);

create table reply
(
	id int auto_increment
		primary key,
	user_id int null,
	post_id int null,
	reply_id int null,
	content varchar(255) null,
	created datetime null,
	updated datetime null
);

create table user
(
	id int auto_increment
		primary key,
	username varchar(32) null,
	password varchar(255) null,
	nickname varchar(255) null,
	document_number varchar(255) null,
	mobile varchar(255) null,
	email varchar(255) null,
	created datetime null,
	updated datetime null,
	constraint username
		unique (username)
);

