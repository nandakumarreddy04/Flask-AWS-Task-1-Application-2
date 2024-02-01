from flask import Flask, render_template

app = Flask(__name__) 


@app.route("/main2") 
def helloworld():
	return "<h1>Hello World, from Nanda-2  (Load Balancer)</h1>"

if __name__ == '__main__':
    app.run(port=5001)
