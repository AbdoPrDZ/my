from flask import Flask, render_template, request
import  json

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/convert")
def convert():
  userNumber = request.args.get('userNumber')
  result = {}
  try:
    result["value"] = bin(int(userNumber))
    result["seccess"] = True
  except:
    result["seccess"] = False
  return json.dumps(result) # dict to str

if __name__ == "__main__":
  app.run(port=80, debug=True)