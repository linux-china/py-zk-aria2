import daemon


def do_main_program():
    pass


with daemon.DaemonContext():
    do_main_program()