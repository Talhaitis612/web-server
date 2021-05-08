from flask import Flask,render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return 'THESE ARE MY THOUGHTS ON BLOG'


@app.route('/about.html')
def about():
    return render_template('about.html')

# @app.route('/favicon')
# def sendIcon():
#     return render_template('about.html')



