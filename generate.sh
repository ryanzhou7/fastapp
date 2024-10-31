#!/bin/zsh

mv ./.git ../.git 
cd ..

# Prompt for additional commands
read -p "Enter a command to execute (or type 'exit' to quit): " user_cmd
if [[ "$user_cmd" == "exit" ]]; then
    echo "Exiting..."
    break
fi
echo "Executing: $user_cmd"
eval $user_cmd

rm -rf ./fastapi/.git
mv ./.git ./fastapi/.git
cd fastapp
git add -A
read -p "Enter git commit " commit
git commit -m "$commit"
git push