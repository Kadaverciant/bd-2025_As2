# Big Data IU-S25 Assignment 2
by Vsevolod Klyushev v.klyushev@innopolis.university

## Requirements

Please, put the `f13` dataset in `data` folder.

## Repository structure
```text
├── data                # Data used in project
├───── cleaned          # Cleaned version of dataset
├──────── *.csv         # Files for PostgreSQL and Neo4j
├──────── *.json        # Files for MongoDB
|
├───── hackolade        # Hackolade data models
├──────── *.hck.json|
|
├── report
├───── report.pdf       # Final report
|
├── screenshots         # Folder to store the screenshots
|
├── scripts             # Folder to store all types of scripts and queries
├───── *.py             # Python scripts
├───── *.sql            # SQL queries
├───── *.js             # MongoDB queries
├───── *.cypher         # Neo4J queries
├───── readme.md        # Script-related suggestions
|
├── README.md 
|
└──
```

## Usefull comands
- `psql -d ecommerce -U postgres -f scripts/load_data_psql.sql`
- `mongosh --file scripts/load_data_mongodb.js`
