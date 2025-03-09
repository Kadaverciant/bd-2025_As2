CREATE INDEX FOR (u:clients) ON (u.user_id);

CREATE INDEX FOR (u:clients) ON (u.client_id);

CREATE INDEX FOR (u:messages) ON (u.client_id);

CREATE INDEX FOR (u:campaigns) ON (u.id);

CREATE INDEX FOR (u:campaigns) ON (u.campaign_type);

CREATE INDEX FOR (u:messages) ON (u.campaign_id);

CREATE INDEX FOR (u:messages) ON (u.message_type);

CREATE INDEX FOR (u:events) ON (u.user_id);

CREATE INDEX FOR (u:events) ON (u.product_id);

CREATE INDEX FOR (u:events) ON (u.category_id);

CREATE INDEX FOR (u:products) ON (u.product_id);

CREATE INDEX FOR (u:categories) ON (u.category_id);

:auto LOAD CSV WITH HEADERS FROM "file:///campaigns.csv" AS row FIELDTERMINATOR ','
call {
    with row
		CREATE (`campaigns`:`campaigns` {
	`id`: toInteger(row.id),
	`campaign_type`: row.campaign_type,
	`channel`: row.channel,
	`topic`: row.topic,
	`started_at`: datetime(REPLACE(row.started_at, ' ', 'T')),
	`finished_at`: datetime(REPLACE(row.finished_at, ' ', 'T')),
	`total_count`: toInteger(row.total_count),
	`ab_test`: toBoolean(row.ab_test),
	`warmup_mode`: toBoolean(row.warmup_mode),
	`hour_limit`: toInteger(row.hour_limit),
	`subject_length`: toInteger(row.subject_length),
	`subject_with_personalization`: toBoolean(row.subject_with_personalization),
	`subject_with_deadline`: toBoolean(row.subject_with_deadline),
	`subject_with_emoji`: toBoolean(row.subject_with_emoji),
	`subject_with_bonuses`: toBoolean(row.subject_with_bonuses),
	`subject_with_discount`: toBoolean(row.subject_with_discount),
	`subject_with_saleout`: toBoolean(row.subject_with_saleout),
	`is_test`: toBoolean(row.is_test),
	`position`: toInteger(row.position)
})} in TRANSACTIONS OF 10000 ROWS;

:auto LOAD CSV WITH HEADERS FROM "file:///messages.csv" AS row FIELDTERMINATOR ','
call {
    with row
		CREATE (`messages`:`messages` {
	`message_id`: row.message_id,
	`campaign_id`: toInteger(row.campaign_id),
	`message_type`: row.message_type,
	`client_id`: toInteger(row.client_id),
	`channel`: row.channel,
	`platform`: row.platform,
	`stream`: row.stream,
	`date`: date(REPLACE(row.date, ' ', 'T')),
	`sent_at`: datetime(REPLACE(row.sent_at, ' ', 'T')),
	`is_opened`: toBoolean(row.is_opened),
	`opened_first_time_at`: datetime(REPLACE(row.opened_first_time_at, ' ', 'T')),
	`opened_last_time_atcopy`: datetime(REPLACE(row.opened_last_time_atcopy, ' ', 'T')),
	`is_clicked`: toBoolean(row.is_clicked),
	`clicked_first_time_at`: datetime(REPLACE(row.clicked_first_time_at, ' ', 'T')),
	`clicked_last_time_at`: datetime(REPLACE(row.clicked_last_time_at, ' ', 'T')),
	`is_unsubscribed`: toBoolean(row.is_unsubscribed),
	`unsubscribed_at`: datetime(REPLACE(row.unsubscribed_at, ' ', 'T')),
	`is_hard_bounced`: toBoolean(row.is_hard_bounced),
	`hard_bounced_at`: datetime(REPLACE(row.hard_bounced_at, ' ', 'T')),
	`is_soft_bounced`: toBoolean(row.is_soft_bounced),
	`soft_bounced_at`: datetime(REPLACE(row.soft_bounced_at, ' ', 'T')),
	`is_complained`: toBoolean(row.is_complained),
	`complained_at`: datetime(REPLACE(row.complained_at, ' ', 'T')),
	`is_blocked`: toBoolean(row.is_blocked),
	`blocked_at`: datetime(REPLACE(row.blocked_at, ' ', 'T')),
	`is_purchased`: toBoolean(row.is_purchased),
	`purchased_at`: datetime(REPLACE(row.purchased_at, ' ', 'T')),
	`created_at`: datetime(REPLACE(row.created_at, ' ', 'T')),
	`updated_at`: datetime(REPLACE(row.updated_at, ' ', 'T'))
})} in TRANSACTIONS OF 10000 ROWS;

:auto LOAD CSV WITH HEADERS FROM "file:///clients.csv" AS row FIELDTERMINATOR ','
call {
    with row
		CREATE (`clients`:`clients` {
	`client_id`: toInteger(row.client_id),
	`user_id`: toInteger(row.user_id),
	`user_device_id`: toInteger(row.user_device_id),
	`email_provider`: row.email_provider,
	`first_purchase_date`: datetime(REPLACE(row.first_purchase_date, ' ', 'T'))
})} in TRANSACTIONS OF 10000 ROWS;

:auto LOAD CSV WITH HEADERS FROM "file:///events.csv" AS row FIELDTERMINATOR ','
call {
    with row
		CREATE (`events`:`events` {
	`event_time`: datetime(REPLACE(REPLACE(row.event_time, ' UTC', ''), ' ', 'T')),
	`event_type`: row.event_type,
	`product_id`: toInteger(row.product_id),
	`category_id`: toInteger(row.category_id),
	`price`: toInteger(row.price),
	`user_id`: toInteger(row.user_id),
	`user_session`: row.user_session
})} in TRANSACTIONS OF 10000 ROWS;

:auto LOAD CSV WITH HEADERS FROM "file:///categories.csv" AS row FIELDTERMINATOR ','
call {
    with row
		CREATE (`categories`:`categories` {
	`category_id`: toInteger(row.category_id),
	`category_code`: row.category_code
})} in TRANSACTIONS OF 10000 ROWS;

:auto LOAD CSV WITH HEADERS FROM "file:///products.csv" AS row FIELDTERMINATOR ','
call {
    with row
		CREATE (`products`:`products` {
	`product_id`: toInteger(row.product_id),
	`brand`: row.brand
})} in TRANSACTIONS OF 10000 ROWS;

:auto LOAD CSV WITH HEADERS FROM "file:///friends.csv" AS row FIELDTERMINATOR ','
CALL {
with row
MATCH (u:clients{user_id:toInteger(row['friend1'])})
MATCH (v:clients{user_id:toInteger(row['friend2'])})
MERGE (u)-[:friends]->(v)-[:friends]->(u)
} in TRANSACTIONS OF 10000 ROWS;

MATCH (m:messages), (c:campaigns)
WHERE m.campaign_id = c.id AND m.message_type = c.campaign_type
MERGE (m)-[:campaigns_to_messages]->(c)-[:campaigns_to_messages]->(m);

MATCH (m:messages), (c:clients)
WHERE m.client_id = c.client_id
MERGE (m)-[:messages_to_clients]->(c)-[:messages_to_clients]->(m);

MATCH (e:events), (c:clients)
WHERE e.user_id = c.user_id
MERGE (e)-[:clients_to_events]->(c)-[:clients_to_events]->(e);

MATCH (e:events), (c:products)
WHERE e.product_id = c.product_id
MERGE (e)-[:events_to_products]->(c)-[:events_to_products]->(e);

MATCH (e:events), (c:categories)
WHERE e.category_id = c.category_id
MERGE (e)-[:events_to_categories]->(c)-[:events_to_categories]->(e);

