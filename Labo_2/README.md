## Doel
In deze opdracht heb ik een keylogger en nmap toegevoegd aan netcat.

### How to use
netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # upload to file
netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135 # echo local text to server port 135
netcat.py -t 192.168.1.108 -p 5555 # connect to server
netcat py -t 192.168.1.108 -p 5555 -l -k ""
netcat py -t 192.168.1.108 -p 5555 -n ""