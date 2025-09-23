<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math Operations Form</title>
</head>
<body>
    <h1>Enter Values for x, y, z</h1>
    <form method="post" action="result.php">
        <label for="x">x:</label>
        <input type="number" step="any" name="x" id="x" required><br><br>
        
        <label for="y">y:</label>
        <input type="number" step="any" name="y" id="y" required><br><br>
        
        <label for="z">z:</label>
        <input type="number" step="any" name="z" id="z" required><br><br>
        
        <button type="submit">Calculate</button>
    </form>
</body>
</html>