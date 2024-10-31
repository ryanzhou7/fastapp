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
python3 -m fastapi_template --name fastapp --api-type rest --db none --orm none

# 2 db - sqlite
python3 -m fastapi_template --name fastapp --api-type rest --db sqlite --orm none --ci none --routers --force --quiet


```
