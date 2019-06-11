import mailroom_oo.cli_main as cli

menu_selection = cli.MenuSelection()
menu_selection = menu_selection.selector()

if __name__ == '__main__':
    menu_selection()
    