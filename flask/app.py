from flask import Flask, request, render_template, session
from redis import Redis

app = Flask(__name__)
app.secret_key = 's'
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    visits = session.get('visits', 0)
    session['visits'] = visits + 1
    return f'Number of visits: {visits + 1}'

if __name__ == '__main__':
    app.run(debug=True)