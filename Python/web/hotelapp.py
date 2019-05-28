from flask import Flask

# step 2
app = Flask(__name__)

#step 3
@app.route("/")  # part 1
def welcome():	 # part 2
    return """ <!DOCTYPE html>
<html>
<body>

<h2>Welcome to DontCome Hotel</h2>
<img src="https://imgstaticcontent.lbb.in/lbbnew/wp-content/uploads/2017/08/31082832/HotelMaris-Anandam1.jpg" alt="Trulli" width="800" height="444">

</body>
</html>
"""

#step 3
@app.route("/plates")  # part 1
def plates():	 # part 2
    return "<b><i>Sphoorthi Oum</b></i> , you see all the plates here are only decoration"

#step 3
@app.route("/aboutus")  # part 1
def aboutus():	 # part 2
    return "Sphoorthi Oum , we are cooks and we cook"

#step 3
@app.route("/contactus")  # part 1
def contactus():	 # part 2
    return "Sphoorthi Oum , no need, after eating who are you"       



# Step 4
if __name__ == "__main__":
    app.run(debug=True)


