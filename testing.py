#!/usr/bin/env python

import sys
import argparse


def main(ip, command):
	with open("/opt/alarms.log") as aw:
		aw.write("{} {}\n".format(ip, command))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Naemon Event handler for True-Sight Integration')
	parser.add_argument('-ip', "--host", required=True, type=str, help='Hostname')
	parser.add_argument('-c', "--command", required=True, type=str, help='Host Output')
	args = vars(parser.parse_args())
	main(args['host'], args['command'])
