import os
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("chmod -R 777 ./")
    if os.path.exists('PingSSR.zip'):os.system('rm -rf PingSSR.zip')
    os.system('pip3 install --target ./package ping3')
    os.chdir('package')
    os.system('zip -r ../PingSSR.zip .')
    os.chdir("..")
    os.system("zip PingSSR.zip lambda_function.py")