# prepare
## install podman
https://podman-desktop.io/

## install podman-compose
```
pip3 install podman-compose
```

# create postgresql server
```
cd infra/local/postgresql
podman-compose -f postgresql.yml up -d
```

# remove postgresql server
```
podman-compose -f postgresql.yml down -v
podman volume rm --all
```

# 操作方法
初期のログイン情報は下記の通りです。

User: postgres  
Password: changeme