# Spawn Mail

This is a simple python script for building an email list for what ever use you may have for a list of emails.

## Getting Started

Simply git clone https://github.com/codebycody/spawn_mail.git and run one of the options listed below to be the proud owner of your very own spawned email list.

### Prerequisites

This script uses python modules
* sys
* os
* getopt
* argparse

### Running the script

By default you can run
```python
  python spawn_mail.py
```
This will output a list of emails in the 'email_list' folder named aolcom.txt. It will pull the list of names from the names folder.


```python
  python spawn_mail.py -n ./path_to_name_file.txt
```
By passing a path value in the -n argument you can set the names that the eamils will be associated with.


```python
  python spawn_mail.py -d 'text.com'
```
By passing a string value in the -d argument you can set the domain name that the emails will be associated with.


```python
  python spawn_mail.py -c 120
```
By passing an int value in the -c argument you can set the number of emails that will be spawned


## Authors

* **Cody Michaels** - *Initial work* - [codebycody](https://github.com/codybycody)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
