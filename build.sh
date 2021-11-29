#git pull
docker rmi sbapp
docker build -t sbapp .
docker stop sbapp
docker rm sbapp
docker run --name sbapp -p 8080:8080 -d --restart always --network dockers_default -e MONGO=mongodb -v /www:/volumes/sbapp  sbapp

