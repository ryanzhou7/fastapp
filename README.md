# Readme

## 1. Creating this

```bash
# github create repo with no readme
poetry new rz_fastapp
cd rz_fastapp
git add -A
# follow github instructions to push up

poetry add "fastapi[standard]"
touch rz_fastapp/main.py
cd rz_fastapp
uvicorn main:app --reload

# same same

# create via cli
python3 -m fastapi_template --name $NAME --api-type rest --db none --ci github --routers --quiet
```

## 2. Containerizing

### Dev with reload

```bash
docker build -t rz-fastapp:1.0 . -f docker/DevDockerfile
docker run -p 8000:8000 --name rz-fastapp rz-fastapp:1.0
docker exec -it rz-fastapp /bin/bash
```

### Dev with mount

```bash
docker build -t rz-fastapp:1.1 . -f docker/MountDockerfile
docker run -it --rm -p 8000:8000 --name rz-fastapp -v $(pwd):/app rz-fastapp:1.1
```

## 4. Router refactor

- Refactor to separate router like [tutorial](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

## 5. Add pydantic-settings

```bash
poetry add pydantic-settings
echo '# environment="test"' > .env
export TAG="1.2"
docker build -t rz-fastapp:$TAG . -f docker/MountVarDockerfile
docker run -it --rm -p 8000:8000 --name rz-fastapp -v $(pwd):/app rz-fastapp:$TAG
# uncomment environment="test" in .env
# stop container and run again
```

## 6. Refactor to main.py

```bash
export TAG="1.3"
docker build -t rz-fastapp:$TAG . -f docker/MountVarDockerfile
docker run -it --rm -p 8000:8000 --name rz-fastapp -v $(pwd):/app rz-fastapp:$TAG
```

## 7. Dumb compose

```bash

docker-compose -f dumb-docker-compose.yml --project-directory . up --build

#docker-compose: This is the Docker Compose command-line tool, which is used to define and run multi-container Docker applications.

#-f dumb-docker-compose.yml: The -f flag specifies the path to the Docker Compose file. In this case, it is dumb-docker-compose.yml.

#--project-directory .: The --project-directory flag sets the project directory. The . indicates the current directory. This is useful for setting the context for relative paths in the Docker Compose file.

# up: The up command builds, (re)creates, starts, and attaches to containers for a service. If the containers do not exist, they will be created. If they already exist, they will be started.

#--build: The --build flag forces the rebuilding of the images before starting the containers. This is useful if you have made changes to the Dockerfile or the application code and want to ensure the latest version is used.

```

## 8. Composing docker compose

```bash

```

# 3. Publishing

- [publishing-docker-images](https://docs.github.com/en/actions/use-cases-and-examples/publishing-packages/publishing-docker-images)
