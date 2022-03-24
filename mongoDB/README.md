# MongoDB

1. Install the python package for client side.
```
python3 -m pip install pymongo
```

2. Start the mongoDB : `docker-compose up`

Chekc the page: 0.0.0.0:8081

### Troubleshooting

If you encounter the port already in used, try this:
```
sudo systemctl stop mongod
systemctl status mongod | grep Active
> Active: inactive (dead)
```
Done