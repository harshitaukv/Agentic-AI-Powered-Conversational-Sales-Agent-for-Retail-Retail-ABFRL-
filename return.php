<?php
session_start();
$orderId = $_SESSION['order_id'] ?? 'Unknown Order';
?>

<!DOCTYPE html>
<html>
<head>
<title>Return / Exchange</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">Return / Exchange</div>

<div class="app">
  <div class="card">
    <h3>Order: <?= $orderId ?></h3>
    <p>👕 Short Sleeve T-Shirt (Qty:1)</p>

    <a class="btn danger" href="confirmation.php">Submit Return</a>
    <a class="btn gray" href="index.php">Cancel</a>
  </div>
</div>

</body>
</html>
