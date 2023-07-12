<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
    <title>Project 4: Guess Start Page</title>
</head>

<body>

    <div class="banner">
        <h1>Guessing Game</h1>
    </div>
    
    <form method="post" action="guess.php">
        <p>
            <input type="hidden" id="num" name="num" value="-1">
            <input type="hidden" id="att" name="att" value="3">
            <input type="hidden" id="rand" name="rand" value=<?php echo rand(1, 10) ?>>
        </p>
        <input type="submit" value="Start Game" class="btn">
    </form>

</body>

</html>