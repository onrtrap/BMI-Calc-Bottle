<!DOCTYPE html>
<html>
	<head>
		<title> BMI Calculator </title>
	</head>
	<body>
	<h1>Please input your Weight (in Pounds) and Height (in Inches)</h1>
	<h2><em>(Do not use Zero or Negative Numbers, Please!!!)<em></h2>

		<form action="/Result" method = POST">
			<label for="weight">Weight:</label>
			<input type="number" id="weight" name="weight"><br><br>
			<label for="height">Height:</label>
			<input type="number" id="height" name="height"><br><br>
			<input type="submit" value="submit">
			</form>
	</body>
</html>