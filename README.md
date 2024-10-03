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
```
