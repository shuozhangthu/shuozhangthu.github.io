import os
os.system('git add .')
os.system('git commit -a -m \'add\' ')
os.system('git push')
os.system('nikola build')
os.system('nikola github_deploy')
