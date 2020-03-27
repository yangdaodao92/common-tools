import paramiko
import select
import re
import sys
import io

# interesting_line_pattern = re.compile('xxx')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def do_tail():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    from os.path import expanduser
    home = expanduser("~")
    # client.connect('xxx', username='xxx', key_filename='%s/.ssh/id_rsa' % home)
    # client.connect('192.168.133.177', username='root', password='123qwe!@#')
    # client.connect('10.126.15.196', username='paas', password='123qwe!@#')
    client.connect('10.126.15.182', username='paas', password='123qwe!@#')

    # log_file = '/opt/tomcats/apache-tomcat-member-center-api/logs/catalina.out'
    log_file = '/opt/apache-tomcat-7.0.47_8080/logs/catalina.out'
    # grep_pattern = "grep_filter"
    remote_command = 'tail -f %s' % log_file
    print(remote_command)

    transport = client.get_transport()
    channel = transport.open_session()
    channel.exec_command(remote_command)

    BUF_SIZE = 1024
    LeftOver = b''
    while transport.is_active():
        # print('transport is active')
        try:
            rl, wl, xl = select.select([channel], [], [], 0.0)
            if len(rl) > 0:
                buf = channel.recv(BUF_SIZE)
                if len(buf) > 0:
                    lines_to_process = LeftOver + buf
                    EOL = lines_to_process.rfind(b'\n')
                    if EOL != len(lines_to_process) - 1:
                        LeftOver = lines_to_process[EOL + 2:]
                        lines_to_process = lines_to_process[:EOL+1]
                    else:
                        LeftOver = b''
                    if lines_to_process.rfind(b'\n') == len(lines_to_process) - 1:
                        for line in lines_to_process.splitlines():
                            print(str(line, 'utf-8'))
                    else:
                        print(len(lines_to_process))

        except (KeyboardInterrupt, SystemExit):
            print('got ctrl+c')
            break
    client.close()
    print('client closed')



if __name__ == '__main__':
    do_tail()
