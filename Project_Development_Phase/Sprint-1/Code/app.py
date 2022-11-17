from flask import Flask, render_template, url_for,request,redirect, Markup, make_response

app=Flask(__name__)



@app.errorhandler(404)
def notFound(e):
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return  render_template('dashboard.html')

@app.route('/Login', methods=['POST',
                              'GET'])
def Login():
    if request.method=='POST':
        return dashboard()
    else:
        return render_template('login.html')




@app.route('/story')
def story():
    return  render_template('story.html')



@app.route('/report')
def report():
    return  render_template('report.html')



if __name__=="__main__":
    app.run()