<?php
session_start();
$orderId = $_SESSION['order_id'] ?? 'Unknown Order';
?>

<!DOCTYPE html>
<html>
<head>
<title>Contact Support</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">Support for <?= $orderId ?></div>

<div class="app">
  <div class="card">
    <h3>How can we help?</h3>

    <a class="btn" href="chat.php">Order Status</a>
    <a class="btn" href="chat.php">Returns</a>
    <a class="btn" href="chat.php">Other</a>

    <a class="btn gray" href="index.php">Back</a>
  </div>
</div>

</body>
</html>
