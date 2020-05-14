from flask import Flask, render_template
import yaml
app = Flask(__name__)

#Load content
with open("./content.yaml") as file:
    content = yaml.full_load(file)
    project_list = content['projects']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html', projects=project_list)

if __name__ == '__main__':
    app.run(debug=True)