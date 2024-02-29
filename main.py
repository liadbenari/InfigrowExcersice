# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from identities import identities_handler


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ids =[{
        'account_name': 'bijihadina',
        'account_id': 233,
        'deal_id': None,
        'email': 'guy@infinigrow.com',
        'contact_id': 1,
    },
    {
        'account_name': 'infinigrow',
        'account_id': 243,
        'deal_id': 23,
        'email': 'dor@infinigrow.com',
        'contact_id': 2,
    },
    {
        'account_name': None,
        'account_id': None,
        'deal_id': 23,
        'email': 'lee@gmail.com',
        'contact_id': None,
    }]
    print(identities_handler(ids))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
