import os
import subprocess
import sys


print sys.argv
github_user = sys.argv[1]
github_repo = sys.argv[2]
heroku_repo = sys.argv[3]

github_string = "git@github.com:" + github_user + "/" + github_repo
heroku_string = "git@heroku.com:" + heroku_repo + ".git"
print heroku_string

subprocess.call(['rm', '-rf', github_repo])
subprocess.call(['git', 'clone', github_string])
os.chdir(os.path.join(os.path.abspath(sys.path[0]), github_repo))
subprocess.call(["git", "push", heroku_string, "master"])
subprocess.call(['rm', '-rf', github_repo])
