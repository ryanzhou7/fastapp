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
docker build -t rz-fastapp:$TAG . -f docker/MountDockerfile
docker run -it --rm -p 8000:8000 --name rz-fastapp -v $(pwd):/app rz-fastapp:$TAG
# uncomment environment="test" in .env
# stop container and run again
```

# 3. Publishing

- [publishing-docker-images](https://docs.github.com/en/actions/use-cases-and-examples/publishing-packages/publishing-docker-images)
