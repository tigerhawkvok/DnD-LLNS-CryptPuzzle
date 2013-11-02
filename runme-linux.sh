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
        echo `You may experience problems running this in an older version of Python.`
        echo `I strongly suggest upgrading to Python 3.`
        read -p `Press [Enter] to continue ...`
        python -i main.py
    fi
fi
