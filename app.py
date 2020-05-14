from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects/')
def projects():
    project_list = [dict()]
    project_list[0]["title"] = "Testy_test"
    project_list[0]["subtitle"] = "Testy testy"
    project_list[0]["description"] = "This is a test"
    project_list[0]["imgsrc"] = "../static/jesse.jpg"
    return render_template('projects.html', projects=project_list)

if __name__ == '__main__':
    app.run(debug=True)