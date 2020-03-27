import paramiko
import pysftp
import select

# ip = '10.126.15.232'
# username = 'paas'
# password = '123qwe!@#'
# base_path = '/tmp/BackUpFile'
# jar_location = ''

ip = '10.125.4.34'
username = 'paas'
password = '234qwe@#$'
base_path = '/tmp/BackUpFile'
jar_location = ''

# ip = '192.168.133.177'
# username = 'root'
# password = '123qwe!@#'
# base_path = '/test/yang'
# jar_location = 'D:\\IdeaSource\\ExploreSelf\\common-tools\\glodon\\data-operation\\build\\libs\\glodon\\'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=ip, username=username, password=password, cnopts=cnopts) as sftp:
    with sftp.cd(base_path):
        sftp.put(jar_location + 'data-operation-2.0.1.jar', 'data-operation-2.0.1.jar')
        sftp.put('.bash_profile', '.bash_profile')
        # out = sftp.execute('source /tmp/BackUpFile/.bash_profile; java -version')
        # print(out)

        # paramiko 执行远程命令
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(ip, username=username, password=password)
        # stdin, stdout, stderr = client.exec_command("bash -lc 'echo $PATH'")
        # stdout = stdout.readlines()

        transport = client.get_transport()
        channel = transport.open_session()
        execute_jar = 'source %s/.bash_profile; cd %s; java -jar data-operation-2.0.1.jar' % (base_path, base_path)
        channel.exec_command(execute_jar)

        BUF_SIZE = 1024
        LeftOver = b''
        while transport.is_active():
            try:
                rl, wl, xl = select.select([channel], [], [], 0.0)
                if len(rl) > 0:
                    buf = channel.recv(BUF_SIZE)
                    if buf != b'\n' and len(buf) > 0:
                        line = str(buf, 'utf-8')
                        print(line.strip('\n'))

                        for tiny_line in line.split('\n'):
                            if tiny_line.find('export filename:') != -1:
                                sftp.get(tiny_line.split('export filename:')[1], tiny_line.split('export filename:')[1])

                        if line.find('Main 已结束') != -1:
                            break

            except (KeyboardInterrupt, SystemExit):
                print('got ctrl+c')
                break

        client.close()
