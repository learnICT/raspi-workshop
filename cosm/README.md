# Cosm

cosm is one of a few online services that can take your data and store it for you. It also makes nice graphs. 
This example posts the number of seconds the raspberry pi has been turned on. The page that shows the data and graphs is here:

https://cosm.com/feeds/120508

If you want to set up your own, then you'd need to make an account and setup a new feed. The feed will need to have a secret key that allows the script to update the feed. The key is stored in a file called api.key

# Other info

You could make this script run every minute by creating a cronjob. Type

crontab -e

And add this line to the end of the file:

* * * * * cd /home/pi/raspi-workshop/cosm; ./update.py

You can find out more about the crontab format here:

man 5 crontab
