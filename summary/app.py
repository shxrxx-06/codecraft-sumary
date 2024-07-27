from flask import Flask , render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', video_filename="cc.mp4")
@app.route('/aboutus')
def abt():
    return render_template('page.html')
@app.route('/dayyy')
def abtday():
    return render_template('day3.html')
@app.route('/day')
def abtdayYY():
    return render_template('day1.html')
@app.route('/dayy')
def abtdaay():
    return render_template('day2.html')
@app.route('/end')
def end():
    return render_template('end.html')

if __name__=='__main__':
    app.run(debug=True)