from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>SERVER IS WORKING!</h1>"

if __name__ == '__main__':
    print("--- Starting Server ---")
    # debug=False disables the reloader, which stops the crashing on Windows
    app.run(debug=False, port=5000)