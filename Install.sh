# Installing required itmes && update...
echo "Calculator Install"
echo "Updating..."
apt update && apt upgrade
echo "UPDATED!"

echo "Installing the required items..."
apt install python
echo "Complete!"

echo "\n"


# Install libraries...
echo "Install libs..."
pip install colorama
echo "\n"
echo "Complete!"
echo "\n"


# Copying files...
echo "Copying files..."
mkdir $PREFIX/share/termux-cal
cp main.py $PREFIX/share/termux-cal
chmod +x $PREFIX/share/termux-cal/main.py
ln -s $PREFIX/share/termux-cal/main.py  $PREFIX/bin/termux-cal

echo "Install Complete!!!"
echo "Now you can run script by typing \"termux-cal\" in the shell!"

