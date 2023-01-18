from ftplib import FTP
from cmd import Cmd
from client import MyClient
import sys


class Interpreter(Cmd):
    prompt = "My-Client> "
    intro = "My FTP Client using Python v0.1"

    def __int__(self):
        Cmd.__init__(self)

    def preloop(self) -> None:
        self.client = MyClient()

    def postloop(self) -> None:
        pass

    def do_pass(self, args: str):
        server_info = 'localhost:21'
        user_info = 'li 123'
        self.client.connect(server_info)
        self.client.login(user_info)

    def do_connect(self, args: str):
        self.client.connect(args)

    def do_login(self, args: str):
        self.client.login(args)

    def do_pwd(self, args: str):
        self.client.pwd(args)

    def do_get(self, args: str):
        self.client.get(args)

    def do_put(self, args: str):
        self.client.put(args)

    def do_cd(self, args: str):
        self.client.cd(args)

    def do_cdup(self, arge):
        self.client.cd('..')

    def do_list(self, args: str):
        self.client.get_file_list(args)

    def do_dir(self, args: str):
        self.client.dir(args)

    def do_ls(self, args: str):
        self.client.dir(args)

    def do_mkdir(self, args: str):
        self.client.mkdir(args)

    def do_rmdir(self,args:str):
        self.client.rmdir(args)

    def do_delete(self, args: str):
        self.client.delete(args)

    def do_rename(self, args: str):
        self.client.rename(args)

    def do_size(self, args: str):
        self.client.get_size(args)

    def do_quit(self, args):
        self.client.quit(args)

    def do_exit(self, args):
        self.client.quit(args)
        sys.exit(0)


if __name__ == '__main__':
    Interpreter().cmdloop()
