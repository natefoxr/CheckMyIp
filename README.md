# This program checks if the External IP from my ISP has been reassigned

## Create a Twilio account and copy your Twilio SID, Twillo Auth token, and Twilio Number

## If the External IP address has changed Twilio will send a text to my personal device with the new External IP address

### Install the following packages in order to run this program:

- `pip3 install twilio`
- `pip3 install dotenv-python`

### To set this up on your own machine, clone the repo and create a .env file with the following infomation:

- `SID="<Twilio SID>"`
- `AUTH="<Twilio Auth token>"`
- `PERSONAL_NUMBER="<The phone number that will recieve notifications>"`
- `TWILIO_NUMBER="<The Twilio number associateds with your account>"`

#### Run the command `python3 check_my_ip.py`

#### To run this program in the background use nohup to have no hangups and the program will run in the background

Run this command `nohup python3 check_my_ip.py &` while in the cloned directory.
The "&" will tell this program to run in the background.

To check if the program is running in the background run `ps x` and you should see the PID and python3 check_my_ip.py.

Alternatively you can run `ps ax | grep check_my_ip.py` to get the PID and see if `python3 check_my_ip.py` is visiable with a "S" label.