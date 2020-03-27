import paramiko
import pysftp
import select

ip = '10.126.15.232'
username = 'paas'
password = '123qwe!@#'
base_path = '/tmp/BackUpFile'

# ip = '192.168.133.177'
# username = 'root'
# password = '123qwe!@#'
# base_path = '/test/yang'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=ip, username=username, password=password, cnopts=cnopts) as sftp:
    with sftp.cd(base_path):
        sftp.put('data-operation-2.0.1.jar', 'data-operation-2.0.1.jar')
        sftp.put('.bash_profile', '.bash_profile')
        # out = sftp.execute('source /tmp/BackUpFile/.bash_profile; java -version')
        # print(out)


# 执行远程命令
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(ip, username=username, password=password)

# client.exec_command("source %s/.bash_profile" % base_path)

# stdin, stdout, stderr = client.exec_command("bash -lc 'echo $PATH'")
# stdout = stdout.readlines()
# client.close()
# output=""
# for line in stdout:
#     output = output + line
# if output != "":
#     print(output)
# else:
#     print("There was no output for this command")

transport = client.get_transport()
channel = transport.open_session()
execute_jar = 'source %s/.bash_profile; cd %s; java -jar data-operation-2.0.1.jar' % (base_path, base_path)
# execute_jar = 'source %s/.bash_profile; java -jar /tmp/BackUpFile/data-operation-2.0.1.jar' % base_path
# execute_jar = '/tmp/BackUpFile/jdk1.8.0_11/java -jar /tmp/BackUpFile/data-operation-2.0.1.jar'
channel.exec_command(execute_jar)

BUF_SIZE = 1024
LeftOver = b''
while transport.is_active():
    try:
        rl, wl, xl = select.select([channel], [], [], 0.0)
        if len(rl) > 0:
            buf = channel.recv(BUF_SIZE)
            if len(buf) > 0:
                print(str(buf, 'utf-8'))
                # print(str(buf, 'utf-8'))
                # lines_to_process = LeftOver + buf
                # EOL = lines_to_process.rfind(b'\n')
                # if EOL != len(lines_to_process) - 1:
                    # LeftOver = lines_to_process[EOL + 2:]
                    # lines_to_process = lines_to_process[:EOL + 1]
                # else:
                    # LeftOver = b''
                # for line in lines_to_process.split(b'\n'):
                    # if str(line, 'utf-8'):
                        # print(line)
                        # print(str(line, 'utf-8'))

    except (KeyboardInterrupt, SystemExit):
        print('got ctrl+c')
        break

client.close()
