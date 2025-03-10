# Big Data IU-S25 Assignment 2
by Vsevolod Klyushev v.klyushev@innopolis.university

## Requirements

Please, put the `f13` dataset in `data` folder.

## Repository structure
```text
├── data                        # Data used in project
├───── cleaned                  # Cleaned versions of dataset
├──────── *.csv                 # Files for PostgreSQL and Neo4j
├──────── *.json                # Files for MongoDB
|
├─────  *.csv                   # Initial data files
|
├── hackolade                   # Hackolade data models
├───── *.hck.json|
|
├── report
├───── Report.pdf               # Final report
├───── Report.tex               # Final report source
├───── IEEEtran.cls             # IEEE LaTeX class 
|
├───── pictures                 # Folder with pictures
├──────── *.png                 # Pictures that are used in report
|
├── screenshots                 # Folder to store the screenshots
|
├── scripts                     # Folder to store all types of scripts and queries
├───── clean_data.ipynb         # Python notebook 
├───── clean_data.py            # Python script for cleaning and storing data
├───── load_data_mongodb.js     # MongoDB script for creating data model and import of data
├───── load_data_neo4j.cypher   # Neo4J script for creating data model and import of data
├───── load_data_psql.sql       # SQL script for creating data model and import of data
├───── neo4j.conf               # Neo4J config file
├───── readme.md                # Script-related suggestions
|
├── README.md 
|
└──
```

## Usefull comands
- `psql -d ecommerce -U postgres -f scripts/load_data_psql.sql`
- `mongosh --file scripts/load_data_mongodb.js`
