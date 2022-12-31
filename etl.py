import pandas as pd

class dbFunctions:
    def __init__(self, cxn, cxn_cursor):
        self.conn = cxn
        self.curs = cxn_cursor


    def load_raw_csv(self):
        f_path = '/var/data/cap3-test00.csv'

        try:
            sql = f"LOAD DATA INFILE \'{f_path}\' INTO TABLE `wireshark_raw` FIELDS TERMINATED BY ',' ENCLOSED BY '\"' IGNORE 1 ROWS;"
            self.curs.execute(sql)
            self.conn.commit()

            print("Success")

        except:
            print("Statement execution error")
            exit(1)


    def create_views(self):
        try:
            sql = """CREATE VIEW `all` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw`;

            CREATE VIEW `arp_all` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `protocol` LIKE 'ARP';

            CREATE VIEW `stp_all` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `protocol` LIKE 'STP';

            CREATE VIEW `udp_all` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `protocol` LIKE 'UDP';

            CREATE VIEW `tcp_all` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `protocol` LIKE 'TCP';

            CREATE VIEW `dns_router` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `source` LIKE '192.168.1.1' AND `protocol` LIKE '%DNS%' ORDER BY `id`;

            CREATE VIEW `ipv6_host` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `source` LIKE '%fe80%' AND `protocol` LIKE '%ICMPv6%' ORDER BY `id`;

            CREATE VIEW `dest_host` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `destination` LIKE '192.168.1.44';

            CREATE VIEW `dest_router` AS 
            SELECT `id`, `source`, `destination`, `protocol`, `length`, `info`
            FROM `wireshark_raw` WHERE `destination` LIKE '192.168.1.1';"""

            self.curs.execute(sql)
            self.conn.commit()

            print("Success")

        except:
            print("Statement execution error")
            exit(1)


    def matching_paths(self):
        try:
            sql = "SELECT COUNT(*) FROM `source_destination`;"
            self.curs.execute(sql)
            self.conn.commit()
            result = self.curs.fetchall()

            r_list = []

            for x in result:
                r_list.append(x)

            df = pd.DataFrame(r_list)

            print(df)

        except:
            print("Statement execution error")
            exit(1)

    def spurious_hosts(self):
        try:
            sql = "SELECT DISTINCT `source` FROM `spurious_tx` ORDER BY `source`;"
            self.curs.execute(sql)
            self.conn.commit()
            result = self.curs.fetchall()

            r_list = []

            for x in result:
                r_list.append(x)

            df = pd.DataFrame(r_list)

            print(df)

        except:
            print("Statement execution error")
            exit(1)


    def detected_protocols(self):
        try:
            sql = "SELECT DISTINCT * FROM `detected_protocols` ORDER BY `protocol`;"
            self.curs.execute(sql)
            self.conn.commit()
            result = self.curs.fetchall()

            r_list = []

            for x in result:
                r_list.append(x)

            df = pd.DataFrame(r_list)

            print(df)

        except:
            print("Statement execution error")
            exit(1)

