from ftplib import FTP


class MyClient(object):
    ftp = FTP()
    host: str = 'localhost'
    port: int = 21
    user: str = 'li'
    password: str = '123'

    def connect(self, args: str):
        port = MyClient.port
        if not args:
            host = MyClient.host
        else:
            server_info = args.split(':')
            host = server_info[0]
            if len(server_info) == 2:
                port = server_info[1]
                try:
                    port = int(port)
                except Exception as err:
                    print(err)
                    print('port error!')
                    return
        try:
            resp = MyClient.ftp.connect(host=host, port=port)
        except Exception as err:
            print(err)
            return
        else:
            print(resp)
            if resp.find('Microsoft') != -1:
                MyClient.ftp.encoding = 'gbk'

    def login(self, args: str):
        if not args.split():
            # user = MyClient.user
            # password = MyClient.password
            user = input('(User Name) ')
            password = input('(Password) ')
        else:
            user_info_list = args.split()
            user = user_info_list[0]
            if len(user_info_list) == 2:
                password = user_info_list[1]
            else:
                password = input('(Password) ')

        try:
            resp = MyClient.ftp.login(user=user, passwd=password)  # Return a string start with 230
        except Exception as err:
            print(err)
            return
        else:
            print(resp)

    def pwd(self, args: str):
        try:
            resp = MyClient.ftp.pwd()  # Return a string
        except Exception as err:
            print(err)
            return
        else:
            print('Remote directory: {}'.format(resp))

    def get(self, args: str):
        # local_file = ''
        # remote_file = ''
        if not args.split():
            remote_file = input("(remote-file) ")
            local_file = input("(local-file) ")
        else:
            file_list = args.split()
            if len(file_list) != 2:
                print('Invalid Syntax.')
                return
            remote_file = file_list[0]
            local_file = file_list[1]
        if remote_file and local_file:
            with open(local_file, 'wb') as f:
                buffer_size = 102400
                try:
                    resp = MyClient.ftp.retrbinary('RETR ' + remote_file, f.write, buffer_size)
                    # done
                except Exception as err:
                    print(err)
                    return
                else:
                    print(resp)
        else:
            print('Invalid Syntax.')
            return

    def put(self, args: str):
        if not args.split():
            local_file = input("(local-file)>")
            remote_file = input("(remote-file)>")
        else:
            file_list = args.split()
            if len(file_list) != 2:
                print('Invalid Syntax.')
                return
            local_file = file_list[0]
            remote_file = file_list[1]
        if remote_file and local_file:
            try:  # FileNotFoundError:
                with open(local_file, 'rb') as f:
                    buffer_size = 102400
                    try:
                        buffer_size = 102400
                        resp = MyClient.ftp.storbinary('STOR ' + remote_file, f, buffer_size)
                    except Exception as err:
                        print(err)
                        return
                    else:
                        print(resp)
            except Exception as err:
                print(err)
                return
        else:
            print('Invalid Syntax.')

    def cd(self, args: str):
        path = args.split()
        if not path:
            remote_path = input('(remote-directory) ')
        else:
            remote_path = path[0]
        try:
            resp = MyClient.ftp.cwd(remote_path)
        except Exception as err:
            print(err)
            return
        else:
            print(resp)

    def dir(self, args: str):
        try:
            resp = self.ftp.dir()
        except Exception as err:
            print(err)
            return
        else:
            # print(resp)
            pass

    def get_file_list(self, args: str):
        try:
            resp = MyClient.ftp.nlst()  # list
        except Exception as err:
            print(err)
            return
        else:
            print(resp)

    def mkdir(self, args: str):
        path = args.split()
        if not path:
            dir_name = input('(directory-name)>')
        else:
            dir_name = path[0]
        try:
            resp = MyClient.ftp.mkd(dirname=dir_name)
        except Exception as err:
            print(err)
            return
        else:
            print(f'257 "{resp}" created')

    def rmdir(self, args: str):
        path = args.split()
        if not path:
            dir_name = input('(directory-name)>')
        else:
            dir_name = path[0]

        try:
            resp = MyClient.ftp.rmd(dirname=dir_name)
        except Exception as err:
            print(err)
            return
        else:
            print(resp)

    def delete(self, args: str):
        name_list = args.split()
        if not name_list:
            file_name = input('(remote-file)>')
        else:
            file_name = name_list[0]

        try:
            resp = MyClient.ftp.delete(filename=file_name)
        except Exception as err:
            print(err)
            return
        else:
            print(resp)

    def rename(self, args: str):  # dir or file all ok
        if not args.split():
            old_name = input('(from-name)>')
            new_name = input('(to-name)>')
        else:
            name_list = args.split()
            old_name = name_list[0]
            new_name = name_list[1]
        try:
            resp = MyClient.ftp.rename(old_name, new_name)
        except Exception as err:
            print(err)
            return
        else:
            print(resp)

    def get_size(self, args: str):
        name_list = args.split()
        if not name_list:
            file_name = input('(remote-file)>')
        else:
            file_name = name_listcl[0]

        try:
            resp = MyClient.ftp.size(file_name)
        except Exception as err:
            print(err)
            return
        else:
            print(f'{file_name}:{resp}')

    def quit(self, args: str):
        try:
            resp = MyClient.ftp.quit()
        except Exception as err:
            self.ftp.close()
            print(err)
            return
        else:
            print(resp)
