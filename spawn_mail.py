import sys, getopt

domain = ''
domain_file = ''

def main(argv):

	def printEmails(emails):
		target = open(domain_file, 'w')

		for email in emails:
			target.write(email)
			target.write('\n')

	for arg in argv[0:]:
		domain = '@' + arg
		domain_file = 'email_lists/' + arg.replace('.', '') + '.txt'

	with open("names/female.first.txt", "r") as ins:
		emails = []
		for line in ins:
			email = line.rstrip('\n') + domain
			emails.append(email)

	printEmails(emails)

	with open("names/male.first.txt", "r") as ins:
		emails = []
		for line in ins:
			email = line.rstrip('\n') + domain
			emails.append(email)

	printEmails(emails)




if __name__ == '__main__':
	main(sys.argv[1:])