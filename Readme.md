# Run with docker 

```shell
docker build -t <imageName> .
docker run --name <containerName> -d -p 80:80 <imageName>
```
### Check container 

```shell
docker logs -f <containerName>
```

# Run with docker-compose

```shell
docker compose up -d
```