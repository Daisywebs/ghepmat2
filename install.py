import launch
import os
import pkg_resources
import sys
import traceback

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

import os

models_dir = os.path.abspath('models/ghepmat2')

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    print(f"ghepmat2 : You can put the model in {models_dir} directory")

print("Check ghepmat2 requirements")
with open(req_file) as file:
    for package in file:
        try:
            python = sys.executable
            package = package.strip()

            if not launch.is_installed(package):
                print(f"Install {package}")
                launch.run_pip(f'install {package}', f"ghepmat2 requirement: {package}")
            elif '==' in package:
                package_name, package_version = package.split('==')
                installed_version = pkg_resources.get_distribution(package_name).version
                if installed_version != package_version:
                    print(f"Install {package}")
                    launch.run_pip(f'install {package}', f"ghepmat2 requirement: changing {package_name} version from {installed_version} to {package_version}")
                
        except Exception as e:
            print(e)
            print(f'Warning: Failed to install {package}, ghepmat2 will not work.')            
            raise e
