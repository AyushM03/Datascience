from flask import Flask


###WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to home page"

@app.route('/about')
def about():
    return "welcome to about page"

@app.route('/contact')
def contact():
    return "welcome to contact page"
#entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
    '''just because of debug=True,
the server will reload itself on code changes and show
a debugger in case an exception happens.'''