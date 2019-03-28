#import Flask Script object
from flask.ext.script import Manager, Server
import main

#init manager boject via app object
manager = Manager(main.app)

#Ctreate a new commands:server
#this command will be run the Flask development_env server
manager.add_command("server",Server())

@manager.shell
def make_shell_conyext():
    """Create a python CLL
    
    return：Default import"object
    type:`dict`
    """
    #确保导入flask app object, 否则启动的CLI 上下文中没有app对象