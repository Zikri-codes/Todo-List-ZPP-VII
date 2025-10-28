
# Variable mhwehehehehe
line: str = '————————————————————————————————————'
running: bool = True
keywords: dict = {
    'add list' : 1,
    'addlist' : 1,
    'add_list' : 1,
    'add-list' : 1,
    'add' : 1,
    '1' : 1,
    
    'remove list' : 2,
    'removelist' : 2,
    'remove_list' : 2,
    'remove-list' : 2,
    'remove' : 2,
    'rmv' : 2,
    '2' : 2,
    
    'see list' : 3,
    'seelist' : 3,
    'see_list' : 3,
    'see-list' : 3,
    'list' : 3,
    'see' : 3,
    'se' : 3,
    '3' : 3,
    
    'exit' : 4,
    'xit' : 4,
    'out' : 4,
    '4' : 4
}
option_list: list = [
    'Add List',
    'Remove List',
    'See List',
    'Exit'
]
main_list: list = []
closing: str = """
░▀█▀░█░█░█▀█░█▀█░█░█░░░█░█░█▀█░█░█
░░█░░█▀█░█▀█░█░█░█▀▄░░░░█░░█░█░█░█
░░▀░░▀░▀░▀░▀░▀░▀░▀░▀░░░░▀░░▀▀▀░▀▀▀
"""
opening: str = """
░▀█▀░█▀█░░░█▀▄░█▀█░░░█░░░▀█▀░█▀▀░▀█▀
░░█░░█░█░░░█░█░█░█░░░█░░░░█░░▀▀█░░█░
░░▀░░▀▀▀░░░▀▀░░▀▀▀░░░▀▀▀░▀▀▀░▀▀▀░░▀░
"""

# function
def see_list():
    if not main_list:
        print('Empty List!')
    else:
        n: int = 1
        print(f'We Had {len(main_list)} Items In The List:')
        for main in main_list:
            print(f'    {n}. {main}')
            n += 1
def remove_list():
    if not main_list:
        print('Empty List!')
    elif len(main_list) == 1:
        print(f'\"{main_list[0]}\" Has Been Removed')
        main_list.pop(0)
    else:
        see_list()
        try:
            user_removed_answer: int = int(input('Which list do you want to be removed?\n (insert number): '))
            if 1 <= user_removed_answer <= len(main_list):
                print(f'\"{main_list[user_removed_answer - 1]}\" Has Been Removed')
                main_list.pop(user_removed_answer - 1)
            else:
                print('Invalid Value!')
        except ValueError:
            print('Something Went Wrong: Please insert a number')
def add_list(add: str):
    main_list.append(add)
    print(f'\"{add}\" Has Been Added To The List')
def distributor(choice: str):
        if choice == 1:
            print(line)
            list_name: str = input('Insert The Name Of The List: ')
            add_list(list_name)
            print(line)
        elif choice == 2:
            print(line)
            remove_list()
            print(line)
        elif choice == 3:
            print(line)
            see_list()
            print(line)
        elif choice == 4:
            print(line)
            print(closing)
            return "exit"
        else:
            print('Something Went Wrong: Invalid Input!')

# opening
print(opening)
print(line)

# loop
while running:
    n: int = 1
    for option in option_list:
        print(f'{n}. {option}')
        n += 1
    user_option_answer: str = input('>> ').lower()
    if user_option_answer in keywords:
        result = distributor(keywords[user_option_answer])
        if result == 'exit':
            running = False
    else:
        print('Something Went Wrong: Invalid Input!')
