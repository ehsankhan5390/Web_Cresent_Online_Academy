@echo off
echo =======================================
echo    Crescent Academy Backup Syncing...  
echo =======================================

cd /d "D:\Project_Automation\Web Cresent Online Academy"

git add .
git commit -m "Auto Backup Update"
git push

echo =======================================
echo     Backup Completed Successfully!    
echo =======================================
pause