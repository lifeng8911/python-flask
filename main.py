from flask import Flask
from config import DevConfig
app = Flask(__name__)

#get the config from object of DevConfig
app.config.from_object(DevConfig)

#指定url路由规则
#当访问url '/' 时为home
@app.route("/")
def home():
    return '<h1> Hello World! <h1>'

if __name__ == '__main__':
    #entry the application
    app.run()
