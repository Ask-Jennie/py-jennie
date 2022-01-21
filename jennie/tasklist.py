import os
from jennie.helper import check_if_angular_project
from jennie.responses import UNKNOWN_PROJECT_TYPE

def install_bootstrap():
    current_dir = os.getcwd()
    if current_dir[:-1] != "/":
        current_dir += "/"

    if check_if_angular_project(current_dir):
        replace = "</head>"
        replace_with = '''  <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css" rel="stylesheet">  
</head>'''
        replace_for_script = "</body>"
        replace_for_script_with = '''  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.min.js"></script>
</body>'''
        dataset = open(current_dir + "src/index.html", "r").read()
        dataset = dataset.replace(replace, replace_with)
        dataset = dataset.replace(replace_for_script, replace_for_script_with)
        open(current_dir + "src/index.html", "w").write(dataset)
    else:
        print (UNKNOWN_PROJECT_TYPE)