def get_event_date(event):
	return event.date

def current_users(events):
	# events.sort(key=get_event_date)
	events.sort(key=lambda event: event.date)

	# for event in events:
	# 	print(event)

	machines = {}

	for event in events:
		if event.machine not in machines:
			machines[event.machine] = set()

		if event.type == "login":
			machines[event.machine].add(event.user)
		elif event.type == "logout" and event.user in machines[event.machine]:
			machines[event.machine].remove(event.user)

		# print(machines)
	
	return machines

def generate_report(machines):
	for machine, users in machines.items():
		if len(users) > 0:
			user_list = ", ".join(users)
			print(f"{machine}: {user_list}")

class Event:
	def __init__(self, event_date, event_type, machine_name, user):
		self.date = event_date
		self.type = event_type
		self.machine = machine_name
		self.user = user
	
	def __str__(self):
		return f"{self.date} {self.type} {self.machine} {self.user}"

	# def __repr__(self):
	# 	return f"{self.date} {self.type} {self.machine} {self.user}"


events = [
	Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
	Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
	Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
	Event('2020-01-22 08:20:01', 'logout', 'myworkstation.local', 'jordan'),
	Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
	Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# for event in events:
# 	print(event)

# print('-------------------------------------------------')

# users = current_users(events)
# print(users)

# generate_report(users)

generate_report(current_users(events))