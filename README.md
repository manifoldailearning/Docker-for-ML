# Docker-for-ML

```
docker --version
docker run hello-world
docker pull busybox
docker images
docker run busybox
docker run busybox echo "hello from busybox mlops"
docker ps
docker ps -a
docker run -it busybox sh
docker rm <container_id>
```


# Other hands on 

```docker run -d -P --name catgif manifoldailearning/catgif
docker ps
docker port catgif
docker stop catgif
docker run -p 8888:5000 manifoldailearning/catgif
docker build -t catgifv2 .
docker run -p 8888:5000 catgifv2
docker login
docker build -t manifoldailearning/catgif-devops .
docker push manifoldailearning/catgif-devops```