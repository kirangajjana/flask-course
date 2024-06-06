from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/pass/<sname>/<int:num>')
def passed(sname,num):
    return f"haiii {sname}, you have passes in exam with {num} marks"
@app.route('/failed/<name>/<int:marks>')
def failed(sname,num):
    return f"sorry {sname}, you are failed in youir exam with {num} marks"    

@app.route('/score/<name>/<int:marks>')
def score(name,marks):
    if marks>50:
        return redirect(url_for('passed',sname=name,num=marks))
    else:
        return redirect(url_for('failed',name,marks))



if __name__=="__main__":
    app.run(debug=True)
