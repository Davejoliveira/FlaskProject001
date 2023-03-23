import paramiko
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['ENV'] = "Development"
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'hello test'


@app.route('/home')
def home():
    return render_template("home.html", )


if __name__ == '__main__':
    app.run()


def callWiki(search):
    search = request.form.get("search")


search = 'Barack Obama'  # Search term
# declare credentials
host = '127.0.0.1'
port = 2222
username = 'user'
password = 'x'
# connect to server
con = paramiko.SSHClient()
con.load_system_host_keys()
con.connect(hostname=host, port=port, username=username, password=password)
stdin, stdout, stderr = con.exec_command('python3 /home/user/Downloads/wiki.py "' + search + '"')
outerr = stderr.readlines()
print("ERRORS: ", outerr)
output = stdout.readlines()
print("output:", output)
for items in output:
    print(items)
