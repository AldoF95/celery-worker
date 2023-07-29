from flask import Flask, render_template
from worker import celery

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/task', methods=['GET'])
def task():
    running = celery.send_task('run_prediction', kwargs={})
    res = celery.AsyncResult(running.id)
    if res.status != 'PENDING':
        print(res.result)
        return res.result
    return 'PENDING'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)