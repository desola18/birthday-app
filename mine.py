 

from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def fun_print():
 	return "The Sea's color is the reflection of the Sky's"

if __name__== '__main__':
 	app.run(debug=True)

  