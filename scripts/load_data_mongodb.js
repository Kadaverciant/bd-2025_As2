db = connect(`mongodb://localhost/ecommerce`);

db.createCollection("campaigns", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "campaigns",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "id": {
                    "bsonType": "number"
                },
                "campaign_type": {
                    "bsonType": "string"
                },
                "channel": {
                    "bsonType": "string"
                },
                "topic": {
                    "bsonType": "string"
                },
                "started_at": {
                    "bsonType": "date"
                },
                "finished_at": {
                    "bsonType": "date"
                },
                "total_count": {
                    "bsonType": "number"
                },
                "ab_test": {
                    "bsonType": "bool"
                },
                "warmup_mode": {
                    "bsonType": "bool"
                },
                "hour_limit": {
                    "bsonType": "number"
                },
                "subject_length": {
                    "bsonType": "number"
                },
                "subject_with_personalization": {
                    "bsonType": "bool"
                },
                "subject_with_deadline": {
                    "bsonType": "bool"
                },
                "subject_with_emoji": {
                    "bsonType": "bool"
                },
                "subject_with_bonuses": {
                    "bsonType": "bool"
                },
                "subject_with_discount": {
                    "bsonType": "bool"
                },
                "subject_with_saleout": {
                    "bsonType": "bool"
                },
                "is_test": {
                    "bsonType": "bool"
                },
                "position": {
                    "bsonType": "number"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});




db.createCollection("events", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "events",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "event_time": {
                    "bsonType": "date"
                },
                "event_type": {
                    "bsonType": "string"
                },
                "product_id": {
                    "bsonType": "number"
                },
                "category_id": {
                    "bsonType": "number"
                },
                "price": {
                    "bsonType": "number"
                },
                "user_id": {
                    "bsonType": "number"
                },
                "user_session": {
                    "bsonType": "string"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});




db.createCollection("friends", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "friends",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "friend1": {
                    "bsonType": "number"
                },
                "friend2": {
                    "bsonType": "number"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});




db.createCollection("clients", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "clients",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "client_id": {
                    "bsonType": "number"
                },
                "user_id": {
                    "bsonType": "number"
                },
                "user_device_id": {
                    "bsonType": "number"
                },
                "email_provider": {
                    "bsonType": "string"
                },
                "first_purchase_date": {
                    "bsonType": "date"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});




db.createCollection("messages", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "messages",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "message_id": {
                    "bsonType": "string"
                },
                "campaign_id": {
                    "bsonType": "number"
                },
                "message_type": {
                    "bsonType": "string"
                },
                "client_id": {
                    "bsonType": "number"
                },
                "channel": {
                    "bsonType": "string"
                },
                "platform": {
                    "bsonType": "string"
                },
                "stream": {
                    "bsonType": "string"
                },
                "date": {
                    "bsonType": "date"
                },
                "sent_at": {
                    "bsonType": "date"
                },
                "is_opened": {
                    "bsonType": "bool"
                },
                "opened_first_time_at": {
                    "bsonType": "date"
                },
                "opened_last_time_at": {
                    "bsonType": "date"
                },
                "is_clicked": {
                    "bsonType": "bool"
                },
                "clicked_first_time_at": {
                    "bsonType": "date"
                },
                "clicked_last_time_at": {
                    "bsonType": "date"
                },
                "is_unsubscribe": {
                    "bsonType": "bool"
                },
                "unsubscribed_at": {
                    "bsonType": "date"
                },
                "is_hard_bounced": {
                    "bsonType": "bool"
                },
                "hard_bounced_at": {
                    "bsonType": "date"
                },
                "is_soft_bounced": {
                    "bsonType": "bool"
                },
                "soft_bounced_at": {
                    "bsonType": "date"
                },
                "is_complained": {
                    "bsonType": "bool"
                },
                "complained_at": {
                    "bsonType": "date"
                },
                "is_blocked": {
                    "bsonType": "bool"
                },
                "blocked_at": {
                    "bsonType": "date"
                },
                "is_purchased": {
                    "bsonType": "bool"
                },
                "purchased_at": {
                    "bsonType": "date"
                },
                "created_at": {
                    "bsonType": "date"
                },
                "updated_at": {
                    "bsonType": "date"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});




db.createCollection("products", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "products",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "product_id": {
                    "bsonType": "number"
                },
                "brand": {
                    "bsonType": "string"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});




db.createCollection("categories", {
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "categories",
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "category_id": {
                    "bsonType": "number"
                },
                "category_code": {
                    "bsonType": "string"
                }
            },
            "additionalProperties": false
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});

var exec = require("child_process").exec;

exec(`mongoimport --db ecommerce --collection campaigns --type json --jsonArray  --file ./data/cleaned/campaigns.json`);
exec(`mongoimport --db ecommerce --collection categories --type json --jsonArray  --file ./data/cleaned/categories.json`);
exec(`mongoimport --db ecommerce --collection clients --type json --jsonArray  --file ./data/cleaned/clients.json`);
exec(`mongoimport --db ecommerce --collection events --type json --jsonArray  --file ./data/cleaned/events.json`);
exec(`mongoimport --db ecommerce --collection friends --type json --jsonArray  --file ./data/cleaned/friends.json`);
exec(`mongoimport --db ecommerce --collection messages --type json --jsonArray  --file ./data/cleaned/messages.json`);
exec(`mongoimport --db ecommerce --collection products --type json --jsonArray  --file ./data/cleaned/products.json`);

