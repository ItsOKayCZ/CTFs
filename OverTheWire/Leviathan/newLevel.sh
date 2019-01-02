mv "Level $1" "Level $1 (DONE)"
mkdir "Level $2"
echo "ssh leviathan$2@leviathan.labs.overthewire.org -p 2223" > "Level $2"/connect.sh
chmod +x "Level $2"/connect.sh
echo "$3" > "Level $2"/password


# 1 2 asdasds