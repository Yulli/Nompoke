import os
print(os.path.dirname(os.getcwd()))
print os.path.dirname(os.getcwd()).join('res')
print os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))).join('res')
