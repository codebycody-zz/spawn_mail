import sys, getopt, argparse

domain = domain_file = email_count = ''

parser = argparse.ArgumentParser()
parser.add_argument('-c', help='int value number of max emails outputted DEFAULT: length of name list')
parser.add_argument('-d', help='str value of the domain associated with the emails DEFAULT: AOL.com')
parser.add_argument('-n', help='str value of the path to name list (one name per line txt file)')
args = parser.parse_args()





def main():

	domain = args.d if args.d else 'aol.com'
	names = args.n
	email_count = args.c if args.c else 'default'
	domain_file = 'email_lists/' + domain.replace('.', '') + '.txt'
	domain = '@' + domain

	def printEmails(emails):
		target = open(domain_file, 'w+')

		for email in emails:
			target.write(email)
			target.write('\n')

	with open(names, "r") as ins:
		emails = []
		for line in ins:
			if email_count != 'default':
				if len(emails) >= int(email_count):
					break

			email = line.rstrip('\n') + domain
			emails.append(email)

	printEmails(emails)
	print('email list done.')

if __name__ == '__main__':
	main()
