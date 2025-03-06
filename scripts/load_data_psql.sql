START TRANSACTION;

CREATE TABLE IF NOT EXISTS campaigns (
	id integer NOT NULL,
	campaign_type text NOT NULL,
	channel text,
	topic text,
	started_at timestamp,
	finished_at timestamp,
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
	event_time timestamp,
	event_type text,
	product_id integer,
	category_id bigint,
	category_code text,
	brand text,
	price real,
	user_id integer,
	user_session text
);

CREATE TABLE IF NOT EXISTS clients (
	client_id bigint PRIMARY KEY,
	user_id integer,
	user_device_id integer,
    email_provider text,
	first_purchase_date timestamp
);

CREATE TABLE IF NOT EXISTS messages (
	message_id text PRIMARY KEY NOT NULL,
	campaign_id integer,
	message_type text,
	client_id bigint,
	channel text,
	platform text,
	stream text,
	date timestamp,
	sent_at timestamp,
	is_opened boolean,
	opened_first_time_at timestamp,
	opened_last_time_at timestamp,
	is_clicked boolean,
	clicked_first_time_at timestamp,
	clicked_last_time_at timestamp,
	is_unsubscribed boolean,
	unsubscribed_at timestamp,
	is_hard_bounced boolean,
	hard_bounced_at timestamp,
	is_soft_bounced boolean,
	soft_bounced_at timestamp,
	is_complained boolean,
	complained_at timestamp,
	is_blocked boolean,
	blocked_at timestamp,
	is_purchased boolean,
	purchased_at timestamp,
	created_at timestamp,
	updated_at timestamp,
	CONSTRAINT fk_clients_client_id_to_messages_client_id FOREIGN KEY (client_id) REFERENCES clients (client_id),
	CONSTRAINT fk_campaigns_to_messages FOREIGN KEY (campaign_id, message_type) REFERENCES campaigns (id, campaign_type)
);

CREATE TABLE IF NOT EXISTS friends (
	friend1 integer,
	friend2 integer
);

\COPY campaigns from './data/postgres/campaigns.csv' delimiter ',' CSV header null as '';
\COPY events from './data/postgres/events.csv' delimiter ',' CSV header null as '';
\COPY clients from './data/postgres/clients.csv' delimiter ',' CSV header null as '';
\COPY messages from './data/postgres/messages.csv' delimiter ',' CSV header null as '';
\COPY friends from './data/postgres/friends.csv' delimiter ',' CSV header null as '';

commit;
