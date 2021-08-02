"""Run python file to be ran inorder to start the API and deploy it on your local computer"""

from main.init import init_app

app = init_app()

if __name__ == '__main__':   #Making sure API is run  when run.py is ran
    app.run(host="0.0.0.0")