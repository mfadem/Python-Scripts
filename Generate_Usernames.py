"""
Generate_Usernames.py
Michael Fadem
4/30/19
Python 3.7.3
Purpose: Generate unique usernames from a given input list of strings.
Restrictions: Usernames must only contain alphanumeric characters (A-Z, a-z, 0-9) and must append a number to the
              username if the username was already added to the unique username list.
Steps:
    1. Pass username list to the generate_users function.
    2. Create variables for the username hash map, unique usernames output and special character regex.
    3. Check length of list to ensure list contains atleast one username
    4. Strip the username using regex of any special characters so only alphanumeric characters remain
    5. Check if the username is in the hash map. If it is, append the appropriate key value number and add the new
       username to the new username list. Otherwise add it to hash map and set key value to 1.
    6. Repeat steps 4 and 5 for all usernames in the input list.
"""

# Import regex library for special character removal from username
import re

"""
Function Name: generate_users
Purpose: Scrub input and create new unique usernames.
"""
def generate_users(usernames):
    # Variables for new username output and regex.
    hash_map = {}
    new_usernames = []
    new_user = ""
    character_regex = '[^A-Za-z0-9]+'

    # Check length of the input list and return if it's empty.
    if len(usernames) == 0:
        print("No Usernames Given!")
        return

    # Increment over the list of the usernames.
    for user in usernames:
        # Strip username of special characters using regex.
        user = re.sub(character_regex, '', user)

        # Continue loop if no valid character remains.
        if user is "":
            continue

        # Check hash map for user name and either increment the counter for the username or add it to the
        # hash map and set the counter to 1. Add new username to new username list.
        if user in hash_map.keys():
            new_user = user + str(hash_map[user])
            new_usernames.append(new_user)
            hash_map[user] += 1
        else:
            new_usernames.append(user)
            hash_map[user] = 1

    print("Original usernames: ", usernames)
    print("New usernames: ", new_usernames, "\n")

    return new_usernames


"""
Function Name: main
Purpose: Driver for the program, calls the generate_users functions.
"""
def main():
    usernames = ["  alice", "bob\n", "__alice__", "alice", 'BoB', 'Alice1', '\tAlice1\t', '!!?!?!']
    generate_users(usernames)
    usernames = ["  alice", "1\tbob", "__ali!c?e__", "AAA", 'BBB', '10101010', '10101010', '  Alic  e1  \t']
    generate_users(usernames)
    usernames = []
    generate_users(usernames)


# Program entry point
if __name__ == '__main__':
    main()