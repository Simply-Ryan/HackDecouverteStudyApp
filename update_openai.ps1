# Update Script for OpenAI Package Fix
# Run this if you encounter: "Client.__init__() got an unexpected keyword argument 'proxies'"

Write-Host "Updating OpenAI and httpx packages to compatible versions..." -ForegroundColor Cyan

# Uninstall conflicting versions
pip uninstall -y openai httpx

# Install compatible versions
pip install openai==1.51.0 httpx==0.27.2

Write-Host "`n✅ Packages updated successfully!" -ForegroundColor Green
Write-Host "You can now run the application with: python app.py" -ForegroundColor Cyan
