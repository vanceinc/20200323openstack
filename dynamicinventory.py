#!/usr//bin/python3

# accept commands fromthe cli
import argparse

# we want to work with json
import json

def main(): 
    inventory = {}  #creatring a dictionary called inventory
    if args.list:  # if the user pass  --list to our script 
        inventory = example_inventory()  # run the function example_inventory
    elif args.host:  # not implemented, if user passes  -- host to the script
        inventory = empty_inventory()
    else:  # if the user does not pass a flag
        inventory = empty_inventory()
    
    print(json.dumps(inventory))  # print inventory dictionary as JSON on the screen


def example_inventory(): 
    return {
        'group': {
            'hosts': ['centurylink-webserver']
            }, 
        'meta': {
           'hostvars': {
               'centurylink-webserver': {
                   'ansible_user': 'centos',
                   'ansible_host': 'localhost'
                       }
                    }
                }
           }

def empty_inventory():
    return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()
    main()
