@echo off
echo "****************************************************"
echo "* Installing TestMy required libraries."
echo "****************************************************"
echo "Installing virtualenv..."
pip install virtualenv
echo "Creating new virtualenv: test_env"
virtualenv test_env
echo "Activating: test_env"
CALL .\test_env\Scripts\activate
echo "Installing behave..."
pip install behave
echo "Installing selenium..."
pip install selenium
CALL .\test_env\Scripts\deactivate
echo "****************************************************"
echo "* Installation done."
echo "****************************************************"


