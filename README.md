## Broadcasting Tutorial with Parent-Children servers

The tutorial is going to walk through you into how to build parent and children broadcasting (one to many)
with `Redis Pub/Sub`

![diagram](assets/parent_children.jpg)

### Prerequisites
* Redis 7.0 +
* Python 3.6 +

Install redis (MAC)
```shell
brew install redis
pip install -r requirements.txt
```
Start redis server

```shell
redis-server
```

Open a new tab in the terminal and run master server

```shell
python server_master.py
```

Open another tab in the terminal and run server a

```shell
python server_a.py
```

After that, start the server b

```shell
python server_b.py
```

Lastly, a new tab for redis-cli
```shell
redis-cli
```

Look into the results as following

* Master server
![master-server](assets/result1.png)

* Server A 
![server-a](assets/result2.png)

* Server B
![server-b](assets/result3.png)

* Redis CLI
![redis-cli](assets/result4.png)

### Author
thadchai.dev@gmail.com