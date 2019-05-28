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
    return """<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Items Unavialable</h2>

<table>
  <tr>
    <th>Dish Name</th>
    <th>Size</th>
    <th>Price</th>
  </tr>
  <tr>
    <td>Biryani</td>
    <td>Full</td>
    <td>30 /-</td>
  </tr>
  <tr>
    <td>Pasta</td>
    <td>small</td>
    <td>20/-</td>
  </tr>
  <tr>
    <td>Juice</td>
    <td>FUll</td>
    <td>50 /-</td>
  </tr>
  <tr>
    <td>Tea</td>
    <td>single</td>
    <td>10/-</td>
  </tr>
   <tr>
    <td>Pasta-veg</td>
    <td>small</td>
    <td>20/-</td>
  </tr>
  <tr>
    <td>Juice with milk</td>
    <td>FUll</td>
    <td>50 /-</td>
  </tr>
  <tr>
    <td>Tea-Ginger</td>
    <td>single</td>
    <td>10/-</td>
  </tr>
</table>

</body>
</html>
"""

#step 3
@app.route("/aboutus")  # part 1
def aboutus():	 # part 2
    return """<!DOCTYPE html>
<html>
<body>

<h1>after eating you'll know</h1>

<p>bye.</p>

</body>
</html>
"""

#step 3
@app.route("/contactus")  # part 1
def contactus():	 # part 2
    return """<!DOCTYPE html>
<html>
<body>

<h2>Contact Us</h2>

<form>
  First name:<br>
  <input type="text" name="firstname">
  <br><br><br><br>
  Your Email:<br>
  <input type="text" name="lastname">
</form>

<p>we wont get back to you</p>


</body>
</html>
"""



# Step 4
if __name__ == "__main__":
    app.run(debug=True)


