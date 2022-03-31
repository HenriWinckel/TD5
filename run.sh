if [ -d "venv" ]
then
    echo "Virtual environnement venv found"
else
    echo "Virtual environnement venv not found, create one"
    python3 -m venv venv
fi

echo "Activating the virtual environement venv"
source ./venv/Scripts/activate

echo "Loading dependencies from requirements.txt"
python3 -m pip install -r requirements.txt

python3 main.py