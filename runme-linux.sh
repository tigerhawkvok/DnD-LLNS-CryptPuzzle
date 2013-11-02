# Shell script
if hash python3 2>/dev/null
then 
python3 -i main.py
else
echo `Attempting to install python 3`
sudo apt-get install python3
if hash python3 2>/dev/null
then 
python3 -i main.py
else
python -i main.py
fi
fi
