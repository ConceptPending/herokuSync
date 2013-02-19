import os
import subprocess
import sys
from flask import Flask, render_template, redirect, request

def githubToHeroku(github_user, github_repo, heroku_repo):
    github_string = "git@github.com:" + github_user + "/" + github_repo
    heroku_string = "git@heroku.com:" + heroku_repo + ".git"

    subprocess.call(['rm', '-rf', github_repo])
    subprocess.call(['git', 'clone', github_string])
    os.chdir(os.path.join(os.path.abspath(sys.path[0]), github_repo))
    subprocess.call(["git", "push", heroku_string, "master"])
    subprocess.call(['rm', '-rf', github_repo])
    return "Success?"

### Flask nonsense
app = Flask(__name__)
app.debug=True

### Hint: Change the below
app.secret_key = r'SuperDuperSecretKey'

# Render and return index.html
@app.route('/')
def index():
    return render_template('index.html')

# Call to push a GitHub repo to Heroku
@app.route('/pushToHeroku', methods=['GET', 'POST'])
@app.route('/pushToHeroku/', methods=['GET', 'POST'])
def pushCall():
    github_user = request.args['github_user']
    github_repo = request.args['github_repo']
    heroku_repo = request.args['heroku_repo']
    
    githubToHeroku(github_user, github_repo, heroku_repo)
    return render_template('index.html')

if __name__ == '__main__':
    # Bing to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
