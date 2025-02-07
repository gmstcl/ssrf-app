from flask import Flask, render_template, request
import urllib.request
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/v1/image')
def get_url():
    url = request.args.get('url', '')

    if url:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = ("data:" + response.headers['Content-Type'] + ";" + "base64," + base64.b64encode(response.read()).decode())
            ret = f"<img src='{data}'/>"
            return (ret)

    return "no param"

@app.route('/v1/health')
def health_check():
    return '{"status": "200 OK"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
