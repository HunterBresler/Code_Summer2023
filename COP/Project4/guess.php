<!DOCTYPE html> <!-- guess.php -->
<html lang="en">

<head>
    <title>Guess a Number</title>
</head>

<body>
    <?php

        if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $randNum = rand(1, 10);
                
        if ($randNum == $_POST["num"]) {
            echo "<h1>Correct!</h1>";
        }
        else {
            echo "<p>No, I was thinking of $randNum.</p>";
        }        
        }
    ?>

    <form method="post" action="guess.php">
        <p>I'm thinking of a number between 1 and 10.</p>
        <p>
            <label for="num">Your guess?</label>
            <input type="number" id="num" name="num" min="1" max="10" autofocus>
        </p>
        <input type="submit" value="Guess">
    </form>
</body>

</html>