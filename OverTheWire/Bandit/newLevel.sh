mkdir "Level $2"
mv "Level $1" "Level $1 (DONE)"
echo "ssh bandit$2@bandit.labs.overthewire.org -p 2220" > "Level $2"/connect.sh
sudo chmod +x "Level $2"/connect.sh
echo $3 > "Level $2"/password

# 6 7 HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
