#!/bin/bash
# automate for start with docker file 
cd BurgerOrderer
docker build -t customer:latest .
cd ..
cd KitchenView
docker build -t kitchen:latest .
cd ..

docker rm -f kitchen customer
docker run -d --name kitchen -v "/Users/chuhathanh/Workspaces/Thanhs Workspaces/PA1489-project/Containers/MenuStore/orders.db":/app/orders.db -p 8001:8001 kitchen:latest
docker run -d --name customer -v "/Users/chuhathanh/Workspaces/Thanhs Workspaces/PA1489-project/Containers/MenuStore/orders.db":/app/orders.db -p 8000:8000 customer:latest