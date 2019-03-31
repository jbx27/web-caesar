from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form =  """
            <!DOCTYPE html>

            <html>
                <head>
                    <style>
                        form {
                            background-color: #eee;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px;
                        }
                        textarea {
                            margin: 10px 0;
                            width: 540px;
                            height:120px;
                        }
                    </style>
                </head>
                <body>
                    <form action="/rotate" method="post">
                        <label for="Rotate by">Rotate by</label>
                        <input type="text" name="rot" value="0"/>
                        <textarea name="text"></textarea>
                        <input type="submit" value="Submit Query"
                        </label>
                    </form>
                </body>
            </html>
        """



@app.route("/")
def index():
    return form

#TODO: encrypt the value of the text parameter using rotate_string
#TODO: return the encrypted string wrapped in <h1> tags to be rendered in the browser
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text= request.form['text']
    encrypted_text = "<h1>" + rotate_string(text, rot) + "</h1>"
    return encrypted_text


app.run()