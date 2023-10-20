import os
from template import TEMPLATE

for dir_name, dir_parameters in TEMPLATE.items():
    new_dir_path = os.path.join(os.getcwd(), dir_name)
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    # if os.path.exists(new_dir_path):
        # os.rmdir(new_dir_path)
