<!DOCTYPE html> <!-- guess.php -->
<html lang="en">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <title>Project 4: Guess Game</title>
</head>

<body>

    <div class="banner">
        <h1>Guessing Game</h1>
    </div>

    <?php

        function _reset()
        {
            $_POST["rand"] = rand(1, 10);
            $_POST["att"] = 3;
        }

        function _print()
        {
            echo "<h3>
            I'm thinking of a number between 1 and 10.
            <br>
            You have <strong>" . $_POST["att"] . "</strong> attemps to guess it.
            </h3>";
        }

        if ($_SERVER["REQUEST_METHOD"] == "POST") 
        {
        
            if ($_POST["num"] == -1)
            {
                _print();
            }
            elseif ($_POST["rand"] == $_POST["num"]) 
            {
                echo "<h2>Correct, the number was " . $_POST["rand"] . "!</h2>";
                _reset();
                _print();
            }
            elseif ($_POST["att"] <= 1)
            {
                echo "<h2>You Lose, the number was " . $_POST["rand"] . ".</h2>";
                _reset();
                _print();
            }
            elseif ($_POST["rand"] > $_POST["num"])
            {
                $_POST["att"]--;
                _print();
                echo "<p>Hint: The number is higher than " . $_POST["num"] . ".</p>";
            } 
            elseif ($_POST["rand"] < $_POST["num"])
            {
                $_POST["att"]--;
                _print();
                echo "<p>Hint: The number is lower than " . $_POST["num"] . ".</p>";
            }         
        }

    ?>

        <form method="post" action="guess.php">
            <p>
                <label for="num">Your guess?</label>
                <input type="number" id="num" name="num" min="1" max="10" autofocus>
                <input type="hidden" id="att" name="att" value=<?php echo $_POST["att"] ?>>
                <input type="hidden" id="rand" name="rand" value=<?php echo $_POST["rand"] ?>>
            </p>
            <input type="submit" value="Guess"  class="btn">
        </form>

</body>

</html>