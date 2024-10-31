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
cd ..
mv ./fastapp/.git ./.git
python3 -m fastapi_template --name fastapp --api-type rest --db none --orm none --ci none --routers --force --quiet
rm -rf ./fastapp/.git
mv ./.git fastapp/.git
cd fastapp
git add -A
git commit -m "1 routers"
git push
```
