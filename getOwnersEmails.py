#!/usr/bin/python

import sys, getopt
import urllib2
import re
import whois



def helptext ():
        print "sample: python getOwnersEmails.py -a www.some.bin/jhdjfhasdkf "
        print ""
        print "	-a\t\tSet full address of bin"
	print "	-p\t\tSet reular expression pattern (optional)"
        exit()


def main (args):
        addr='https://somebin.com/dkkskfhsw';
	pattern='https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+.co.il';

        pname = args[0]
        i = 1
        if len(args) == 1:
                helptext()
        while i < len(args):
                a = args[i]

                if a == "--help":
                        helptext();
                elif a == "-a":
                        i += 1
                        addr = args[i];
                elif a == "-p":
                        i += 1
                        pattern = args[i];

                else:
                        print "Invalid argument '%s'" % args[i]
                        exit()

                i += 1

	response = urllib2.urlopen(addr)
	html = response.read()

	urls = re.findall(pattern, html)
	unic_urls = set(urls)
	unic_urls_list = list(unic_urls)


	emails =[];
	for url in unic_urls_list:
		w=whois.whois(url);
		if isinstance(w.emails, list):
			for email in w.emails:
				emails.append(email);
		else:
			emails.append(w.emails);

	emails_set = set(emails);
	emails_unic=list(emails_set);

	for email in emails_unic:
		print email;


main(sys.argv)
exit()

