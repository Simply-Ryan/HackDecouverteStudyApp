#!/bin/bash
# Update Script for OpenAI Package Fix
# Run this if you encounter: "Client.__init__() got an unexpected keyword argument 'proxies'"

echo -e "\033[0;36mUpdating OpenAI and httpx packages to compatible versions...\033[0m"

# Uninstall conflicting versions
pip uninstall -y openai httpx

# Install compatible versions
pip install openai==1.51.0 httpx==0.27.2

echo -e "\n\033[0;32m✅ Packages updated successfully!\033[0m"
echo -e "\033[0;36mYou can now run the application with: python app.py\033[0m"
