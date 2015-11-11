# Steam Master Fapper
This python script show number of hours spent to play on steam in the last 2 weeks.

# Installation
 
Pip is required, install it first 
```
apt-get install python-pip
```
Install some Python libs.
```
pip install pyyaml
pip install requests
pip install tabulate
pip install Django==1.7.10
```

Clone the project
```
git clone https://github.com/Sispheor/SteamMasterFapper
```
Open the file **settings.yml** in the root of the project and edit it accordingly to your steam account and your friends IDs.

# Usage
Print the report in your current shell
```
python smf.py --text
```
Send the report by mail
```
python smf.py --mail
```

You can add it to your crontab to send it automatically and recurrently.
Edit your crontab
```
crontab -e
```

Add this line to send it for example each sunday at 8 PM.
```
* 20 * * 0 python /path/to/steammasterfapper/smf --mail >/dev/null 2>&1
```