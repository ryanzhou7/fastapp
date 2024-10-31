#!/bin/zsh

cp -r ./.git ../.git
cd ..

while true; do
  echo "Enter flags to execute (or type 'exit' to quit): "
  read flags
  if [[ "$flags" == "exit" ]]; then
      echo "Exiting..."
      break
  fi
  echo "Executing: $flags"
  eval python3 -m fastapi_template --name fastapp $flags
  break
done

rm -rf ./fastapp/.git
cp -r ./.git ./fastapp/.git
rm -rf ./.git
cd fastapp
# git add -A

# while true; do
#   echo "Enter git commit "
#   read commit_message
#   break
# done

# git commit -m "$commit_message"
# git push