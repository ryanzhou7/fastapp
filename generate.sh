#!/bin/zsh

cp -r ./.git ../.git
cd ..

while true; do
  echo "Enter a command to execute (or type 'exit' to quit): " user_cmd
  read user_cmd
  if [[ "$user_cmd" == "exit" ]]; then
      echo "Exiting..."
      break
  fi
  echo "Executing: $user_cmd"
  eval $user_cmd
  break
done

rm -rf ./fastapp/.git
cp -r ./.git ./fastapp/.git
rm -rf ./.git
cd fastapp
git add -A

while true; do
  echo "Enter git commit " commit_message
  read commit_message
  break
done

git commit -m "$commit_message"
git push