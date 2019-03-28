#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#import Flask Script object
from flask_script import Manager, Server
import main

#init manager boject via app object
manager = Manager(main.app)

#Ctreate a new commands:server
#this command will be run the Flask development_env server
manager.add_command("server",Server())

@manager.shell
def make_shell_conyext():
     """ Create a python CLI
        
    return：Default import"object
    type:`Dict`
    """
    #确保导入flask app object, 否则启动的CLI 上下文中没有app对象
     return dict(app=main.app)

if __name__ == '__main__':
    manager.run()
