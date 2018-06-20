@echo off
echo "****************************************************"
echo "* Running TestMy..."
echo "****************************************************"
CALL .\test_env\Scripts\activate
set PATH=%PATH%;%CD%\libs
behave
CALL .\test_env\Scripts\deactivate
echo "****************************************************"
echo "* Done"
echo "****************************************************"

