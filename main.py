from flask import Flask

app=Flask(__name__)

if __name__=='__main__':
    print("Starting server: %d"%9089)
    app.run(port=9089)