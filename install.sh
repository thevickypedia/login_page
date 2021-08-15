#!/bin/bash

# Checks brew installation
brew_check=$(which brew)
brew_condition="/usr/local/bin/brew"
if [[ "$brew_check" != "$brew_condition" ]]; then
  echo "Installing Homebrew"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  else echo "Found Homebrew, skipping installation"
fi

# Installs npm
brew install npm

# Installs JavaScript Obfuscator
npm install --save-dev javascript-obfuscator

# Links JavaScript Obfuscator
npm link javascript-obfuscator
