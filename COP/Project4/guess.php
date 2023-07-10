<!DOCTYPE html> <!-- guess.php -->
<html lang="en">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <title>Project 4: Quiz</title>
</head>

<body>

    <?php

        $randNum = rand(1, 10);
        $attemps = 3;

        if ($_SERVER["REQUEST_METHOD"] == "POST") 
        {
                    
            if ($randNum == $_POST["num"]) 
            {
                echo "<h1>Correct!</h1>";
                $randNum = rand(1, 10);
                $attemps = 3;
            }
            elseif ($attemps <= 0)
            {
                echo "<p>You're out of attemps.<br>The number was $randNum.</p>";
                $randNum = rand(1, 10);
                $attemps = 3;
            }
            elseif ($randNum > $_POST["num"])
            {
                echo "<p>Hint: The number is higher than that.</p>"
                $attemps--;
            } 
            elseif ($randNum < $_POST["num"])
            {
                echo "<p>Hint: The number is lower than that.</p>"
                $attemps--;
            }         
        }
    ?>

    <form method="post" action="guess.php">
        <p>
            I'm thinking of a number between 1 and 10.
            <br>
            You have $attemps to guess it.
        </p>
        <p>
            <label for="num">Your guess?</label>
            <input type="number" id="num" name="num" min="1" max="10" autofocus>
        </p>
        <input type="submit" value="Guess">
    </form>
</body>

</html>