from flask import Flask, request, escape

# Init application
app=Flask(__name__)

# Welcome endpoint
@app.route('/hello')
def newFunction():
    print("Local check")
    name=request.args.get('name','John')
    return f"Hello , {escape(name)}"

# Initialize application
if __name__=='__main__':
    print("Starting server: %d"%9089)
    app.run(port=9089)