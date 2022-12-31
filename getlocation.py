import os
import json

class location():

    def curl_ip(ip):

#        cmd = "git --version"
        cmd = f"curl http://ipinfo.io/{ip}"

        os.system(cmd)
#        returned_value = os.system(cmd)  # returns the exit code in unix
#        print('returned value:', returned_value)

    def ip_dict(json):
        with open(json) as ci:
            d = json.load(ci)

