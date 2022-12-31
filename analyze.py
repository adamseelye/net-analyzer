from etl import dbFunctions
import connector
import pandas as pd
import filepath
import getlocation


try:
    connection = connector.db_connect.db_connection()
    conn_obj = dbFunctions(connection[0], connection[1])
except:
    print("Database connection error")
    exit(1)


print("Hello and welcome! Let's analyze some Wireshark data!\n")

def main_menu():
    print("1. Display detected protocols")
    print("2. Load raw data into database")
    print("3. How many entries have matching sources and destinations?")
    print("4. List of hosts sending spurious retransmissions")


    action = input("Please choose which action to take: ")

    if action == "1":
        print("Detected Protocols: ")

        try:
            conn_obj.detected_protocols()

        except:
            print("Data load error, please restart program")
            exit(1)

    elif action == "2":
        print("Loading raw Wireshark data into database. May take some time...")

        try:
           conn_obj.load_raw_csv()
           conn_obj.create_views()
           print("Success")

        except:
            print("Data load error, please restart program")
            print("Database corruption possible")
            exit(1)

    elif action == "3":
        print("Number of matching source/destination entries: ")

        try:
            print("Displaying Data")
            conn_obj.matching_paths()

        except:
            print("Data display error, please restart program")
            exit(1)


    elif action == "4":
        print("Hosts sending spurious retransmissions: ")

        try:
            conn_obj.spurious_hosts()

        except:
            ("Data display error, please restart program")
            exit(1)

    elif action == "5":
        ip = input("Please enter the IP on which you would like to gather data: ")

        try:
            loc_ip = getlocation.location.curl_ip(ip)
            loc_dict = getlocation.location.ip_dict(ip)

        except:
            print("Command execution error")
            exit(1)

main_menu()

