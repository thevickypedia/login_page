rm -rf package.json package-lock.json node_modules

clear
echo "*****************************************************************************************************************"
echo "Node Modules and packages were removed."
echo "*****************************************************************************************************************"

read -p "Do you want to proceed and uninstall JavaScript Obfuscator? <Y/N> " prompt
if [[ $prompt =~ [yY](es)* ]]
then
  npm unlink javascript-obfuscator
  npm uninstall javascript-obfuscator
  echo "***************************************************************************************************************"
  echo "Uninstalled JavaScript Obfuscator"
  echo "***************************************************************************************************************"
else
  echo "Skipped to uninstall Obfuscator."
  exit
fi

read -p "Do you want to proceed and uninstall Node (npm)? <Y/N> " prompt
if [[ $prompt =~ [yY](es)* ]]
then
  brew uninstall npm
  echo "***************************************************************************************************************"
  echo "Uninstalled NodeJS."
  echo "***************************************************************************************************************"
else
  echo "Skipped to uninstall NodeJS."
fi
