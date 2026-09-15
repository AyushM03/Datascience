from flask import Flask, render_template, request

app = Flask(__name__)

#variable rules if parameter is passed as any type like int float etc,
#the default type is string, so if you want to pass any other type
#you have to specify it in the route
@app.route('/maths/<inputs>', methods=['GET', 'POST'])
def maths(inputs):
    if request.method == 'POST':
        # Process the POST request data
        data = request.form.get('data')
        return f"Received POST data: {data}"
    else:
        # Handle GET request
        return render_template('maths.html', results=inputs)


@app.route('/success/<inputs>')
def success(inputs):
    if inputs == '1':
        result = 'one'
    exp={
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five'
    }
    return render_template('result1.html', results=exp)

if __name__ == '__main__':
    app.run(debug=True)