START TRANSACTION;

CREATE TABLE IF NOT EXISTS campaigns (
	id integer NOT NULL,
	campaign_type text NOT NULL,
	channel text,
	topic text,
	started_at date,
	finished_at date,
	total_count integer,
	ab_test boolean,
	warmup_mode boolean,
    hour_limit integer,
	subject_length integer,
	subject_with_personalization boolean,
	subject_with_deadline boolean,
	subject_with_emoji boolean,
	subject_with_bonuses boolean,
	subject_with_discount boolean,
	subject_with_saleout boolean,
	is_test boolean,
	position integer,
	PRIMARY KEY (id, campaign_type)
);

CREATE TABLE IF NOT EXISTS events (
	event_time date,
	event_type text,
	product_id integer,
	category_id bigint,
	category_code text,
	brand text,
	price real,
	user_id integer,
	user_session text
);

CREATE TABLE IF NOT EXISTS client_first_purchase_date (
	client_id bigint PRIMARY KEY NOT NULL,
	first_purchase_date date,
	user_id integer,
	user_device_id integer
);

CREATE TABLE IF NOT EXISTS messages (
	id integer PRIMARY KEY NOT NULL,
	message_id text,
	campaign_id integer,
	message_type text,
	client_id bigint,
	channel text,
	category text,
	platform text,
	email_provider text,
	stream text,
	date date,
	sent_at date,
	is_opened boolean,
	opened_first_time_at date,
	opened_last_time_at date,
	is_clicked boolean,
	clicked_first_time_at date,
	clicked_last_time_at date,
	is_unsubscribed boolean,
	unsubscribed_at date,
	is_hard_bounced boolean,
	hard_bounced_at date,
	is_soft_bounced boolean,
	soft_bounced_at date,
	is_complained boolean,
	complained_at date,
	is_blocked boolean,
	blocked_at date,
	is_purchased boolean,
	purchased_at date,
	created_at date,
	updated_at date,
	user_device_id integer,
	user_id integer,
	CONSTRAINT fk_client_first_purchase_date_client_id_to_messages_client_id FOREIGN KEY (client_id) REFERENCES client_first_purchase_date (client_id)
);

CREATE TABLE IF NOT EXISTS friends (
	friend1 integer NOT NULL,
	friend2 integer NOT NULL
);

\COPY campaigns from './data/campaigns_cleaned.csv' delimiter ',' CSV header null as '';
\COPY events from './data/events.csv' delimiter ',' CSV header null as '';
\COPY client_first_purchase_date from './data/client_first_purchase_date.csv' delimiter ',' CSV header null as '';
\COPY messages from './data/messages_cleaned.csv' delimiter ',' CSV header null as '';
\COPY friends from './data/friends.csv' delimiter ',' CSV header null as '';

commit;
