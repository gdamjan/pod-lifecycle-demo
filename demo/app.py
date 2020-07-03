from flask import Flask, render_template, redirect, url_for, Response
import sys, os, time, signal


app = Flask(__name__)


if 'CONFIG_INIT_DELAY' in os.environ:
    try:
        init_wait = int(os.environ['CONFIG_INIT_DELAY'])
    except:
        pass
    time.sleep(init_wait)

# poor mans global state
GLOBAL_STATE = {
    'counter': 0,
    'version': os.environ.get('VERSION', 'unspecified'),
}

@app.route('/health')
def health():
    return 'ok', 200


@app.route('/')
def index():
    return render_template('index.html', GLOBAL_STATE=GLOBAL_STATE)

@app.route('/increment', methods=['POST'])
def inc():
    GLOBAL_STATE['counter'] += 1
    return redirect(url_for('index'))

@app.route('/decrement', methods=['POST'])
def dec():
    GLOBAL_STATE['counter'] -= 1
    return redirect(url_for('index'))


@app.route('/hang', methods=['POST'])
def hang():
    def _gen():
        yield 'hang up now'
        os.kill(os.getpid(), signal.SIGSTOP)
    return Response(_gen(), mimetype='text/plain')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    def _gen():
        yield 'shut down now'
        os._exit(1)
    return Response(_gen(), mimetype='text/plain')
