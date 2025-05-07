from flask import Flask, render_template, send_file
app = Flask(__name__)

@app.get('/')
def home():
   return render_template('cli_ccy.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5008)