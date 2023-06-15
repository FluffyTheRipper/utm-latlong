
if __name__ == '__main__':
    pass

def yes_or_no(prompt):
    while True:
        ans = input(f'{prompt} (y/n):')

        if ans.lower()  in ['y', 'yes']:
            return True
        
        if ans.lower() in ['n', 'no']:
            return False
        
def select_column(target, max):
    while True:
        ans = input(f'Select {target} column (0-{max}):')

        if 0 <= int(ans) <= max:
            return int(ans)
