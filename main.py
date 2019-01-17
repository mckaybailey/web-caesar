from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form method='POST' action='/form-inputs'>

        <label>Rotate by:
            <input name="rot" type="text" value="0" />
        </label>
        
        <label>
            <textarea name="text" >{0}</textarea>
        </label>
        
        
        
        <input type="submit" />
        
</form>
    </body>
</html>"""
@app.route("/")
def index():
    new = form.format("{0}")
    return new

@app.route("/form-inputs", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    texts = str(request.form['text'])
    resp = rotate_string(texts, rotate) 
    resp = form.format(resp)
    return resp
    #return "<h1>" + resp + "</h1>"

@app.route("/hello")
def hello():
    firstname = request.args.get("firstname")
    return '<h1>Hello, '+ firstname + '</h1>'

app.run()