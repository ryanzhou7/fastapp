# Commands

```zsh
# 0
python3 -m fastapi_template --name fastapp --api-type rest --db none --orm none --ci none --quiet
cd fastapp
rm -rf .git
git branch -M main
git remote add origin https://github.com/ryanzhou7/fastapp.git
git push -u origin main

# 1 routers
--api-type rest --db none --orm none

# 2 db - sqlite
--api-type rest --db sqlite --orm none --ci none --routers --force --quiet

# 3 orm
--api-type rest --db sqlite --orm sqlalchemy --ci none --routers --force --quiet

# 4 dummy model
--api-type rest --db sqlite --orm sqlalchemy --ci none --routers --dummy --force --quiet

# 5 migrations
--api-type rest --db sqlite --orm sqlalchemy --ci none --routers --dummy --migrations --force --quiet

# 6 postgresql
--api-type rest --db postgresql --orm sqlalchemy --ci none --routers --dummy --migrations --force --quiet

# 7 gunicorn
--api-type rest --db postgresql --orm sqlalchemy --ci none --routers --dummy --migrations --gunicorn --force --quiet

# 8 ci github
--api-type rest --db postgresql --orm sqlalchemy --ci github --routers --dummy --migrations --gunicorn --force --quiet
```
