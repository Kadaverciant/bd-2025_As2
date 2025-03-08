When you'll run `load_data_mongosh.js` the imports might not work out. In that case, please, 
just run the following lines by yourself in terminal. As bonus, you'll be able to see a progress bar:)

(I am not js guru, so I've not been able to solve this issue. With csv everything worked, but since mongo can't parse bool and date info from csvs properly I had to migrate to jsons)

- `mongoimport --db ecommerce --collection campaigns --type json --jsonArray  --file ./data/cleaned/campaigns.json`
- `mongoimport --db ecommerce --collection categories --type json --jsonArray  --file ./data/cleaned/categories.json`
- `mongoimport --db ecommerce --collection clients --type json --jsonArray  --file ./data/cleaned/clients.json`
- `mongoimport --db ecommerce --collection events --type json --jsonArray  --file ./data/cleaned/events.json`
- `mongoimport --db ecommerce --collection friends --type json --jsonArray  --file ./data/cleaned/friends.json`
- `mongoimport --db ecommerce --collection messages --type json --jsonArray  --file ./data/cleaned/messages.json`
- `mongoimport --db ecommerce --collection products --type json --jsonArray  --file ./data/cleaned/products.json`