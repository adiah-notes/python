#!/usr/bin/env python3

import csv
import operator
import re
import sys


def main():

	error_messages, user_stats = parse_log_file(sys.argv[1])

	error_messages = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)
	user_stats = sorted(user_stats.items())

	message_list = []

	for message in error_messages:
		message_list.append({
			'Error': message[0],
			'Count': message[1]
		})

	with open('error_message.csv', 'w') as errors:
		writer = csv.DictWriter(errors, fieldnames=['Error', 'Count'])
		writer.writeheader()
		writer.writerows(message_list)

	user_list = []

	for user in user_stats:
		user_list.append({
			'Username': user[0],
			'INFO': user[1]['info'],
			'ERROR': user[1]['error']
		})

	with open('user_statistics.csv', 'w') as stats:
		writer = csv.DictWriter(stats, fieldnames=['Username', 'INFO', 'ERROR'])
		writer.writeheader()
		writer.writerows(user_list)

def parse_log_file(logfile):
	error_messages = {}
	user_stats = {}

	sample_dictionary = {
		'error': 'Timeout while retrieving information',
		'count': 15,
	}

	sample_users = {
		'user': 'ac',
		'error': 2,
		'info': 2,
	}

	with open(logfile, 'r') as log:

		for line in log:
			# Check if the log lines match the regex
			result = re.search(
				r"^([A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2}) [\w\.]* ticky: (INFO|ERROR) ([\w\' ]*) (\[#\d+\] )?\((.*)\)$",
				line
			)

			if result:
				# Once the log line matches, get the info
				_, status, info, _, user = result.groups()

				if user not in user_stats:
					user_stats[user] = {'error': 0, 'info': 0}

				if status == 'ERROR':
					user_stats[user]['error'] += 1

					if info not in error_messages:
						error_messages[info] = 0

					error_messages[info] += 1

				if status == 'INFO':
					user_stats[user]['info'] += 1

	return error_messages, user_stats



if __name__ == '__main__':
	main()
