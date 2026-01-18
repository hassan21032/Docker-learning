from flask import Flask
import redis

app = Flask(__name__)

# Create Redis connection (once)
r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

@app.route('/')
def welcome():
    return "Welcome to my redis app!"

@app.route('/count')
def count():
    visits = r.incr("visits")
    return f"Visit count: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
