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
docker-compose -f dumb-docker-compose.yml --project-directory . up --build
# reload should still work even though we changed
settings.py
  reload: bool = False
# because this variable is overwritten by

docker-compose.yml
# Set environment variables for the container
environment:
  # Set the HOST environment variable to '0.0.0.0'
  # This typically means the application will listen on all network interfaces
  HOST: 0.0.0.0

  # Enables autoreload.
  RELOAD: "True"
```

- Now set the RELOAD: "False"
- `docker-compose -f dumb-docker-compose.yml --project-directory . up --build`
- There should be no reload now

- Now adjacent to dumb-docker-compose.yml add `docker-compose.dev.yml`

```yml
services:
  api:
    # Set environment variables for the container
    environment:
      # Enables autoreload.
      RELOAD: "True"
```

- `docker-compose -f dumb-docker-compose.yml -f docker-compose.dev.yml --project-directory . up --build`
- Reload should work now

## 9. Cleaning up

1. New prod ready Dockerfile
2. Rename `dumb-docker-compose.yml` -> `docker-compose.yml`
3. Delete all \*Dockerfile in docker/
4. Move `docker-compose.dev.yml` to new deploy/ dir
5. Move relevant dev `docker-compose.yml` configs to `docker-compose.dev.yml`
6. Add `.dockerignore`

```bash
# command for deploying in prod
# should build fine and run but no port is exposed
docker-compose up --build
```

If you want to develop in docker with autoreload and exposed ports add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose build
```

## 10. Add dev tools

### Add ruff as a linter / formatter

- https://docs.astral.sh/ruff/editors/setup/
  - Just install the vscode extension
- `poetry add --group dev ruff`
- See ruff [rules](https://docs.astral.sh/ruff/rules/) you can turn on, note the ones that can auto fix
- Add this to ruff.toml though it can also go in pyproject.toml

```toml
[lint]
select = [
    "I", # isort, auto sorts imports
]
```

To see this work, update your code like

```python
from rz_fastapp.web.api.health import router as health_router
from fastapi import FastAPI
```

- `poetry run ruff check`
  - shows errors
- `poetry run ruff check --fix`
  - will auto fix
- Now just add the rest in the next commit, read through the examples
- Now turn off specific rules

```toml
[lint]
# select = [...] selection
ignore = [
  "D100",
  "D104",
  "S104",
  "D401",
]
```

### Pre-commit hook

Now we want to make ruff run prior to every commit

```bash
poetry add --group dev pre-commit
touch .pre-commit-config.yaml
poetry run pre-commit install

# Run Pre-Commit Manually (Optional):
# You can run the pre-commit hooks manually on all files to ensure they are formatted correctly:
# this respects the .gitignore
poetry run pre-commit run --all-files
```

### Add a type checker

- Read about [ruff vs mypy](https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-mypy-or-pyright-or-pyre)
- read about [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html)
- `poetry add --group dev mypy`
- add to pyproject.toml

```toml
[tool.mypy]
python_version = "3.10"
ignore_missing_imports = true
strict = true
```

- `poetry run mypy rz_fastapp`
  - manually run
- error that would be detected

```python
@router.get("/health")
def health_check() -> None:
    return {"message": "Hello world"}
```

- To add to pre-commit, add to pyproject.toml

```toml
      - id: mypy
        name: Check types with MyPy # A descriptive name for the hook.
        entry: poetry run mypy # The command to run when the hook is triggered. It runs MyPy using Poetry.
        language: system # Specifies that the hook uses the system's language environment.
        types: [python] # Specifies the file types that the hook should run on.
        args: ["rz_fastapp", "--ignore-missing-imports"] # Additional arguments for MyPy.
```

## Appendix

- git log
- git show commit1..commit2 > diff.log
- Based on this git show commit1..commit2 tell a summarize of this commit did.
- Based on this git show commit1..commit2, output step by step instructions that a beginner learning fastapi would understand to get to this commit.

- [publishing-docker-images](https://docs.github.com/en/actions/use-cases-and-examples/publishing-packages/publishing-docker-images)

```

```
