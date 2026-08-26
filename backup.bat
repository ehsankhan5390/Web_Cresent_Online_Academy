@echo off
echo =======================================
echo    Crescent Academy Backup Syncing...  
echo =======================================

cd /d "D:\Project_Automation\Web Cresent Online Academy"

git add .
git commit -m "Auto Backup Update" --allow-empty
git push -u origin main --force

echo =======================================
echo     Backup Completed Successfully!    
echo =======================================
pause