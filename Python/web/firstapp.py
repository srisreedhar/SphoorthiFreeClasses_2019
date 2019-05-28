from flask import Flask

# step 2
app = Flask(__name__)

#step 3
@app.route("/")  # part 1
def hello():	 # part 2
    return "Sphoorthi Oum , This is my first webpage"

# Step 4
if __name__ == "__main__":
    app.run(debug=True)


