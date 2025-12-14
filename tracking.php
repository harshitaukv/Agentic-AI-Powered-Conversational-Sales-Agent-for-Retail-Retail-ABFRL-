<?php
session_start();
$orderId = $_SESSION['order_id'] ?? 'Unknown Order';
?>

<!DOCTYPE html>
<html>
<head>
<title>Tracking</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">Order Tracking</div>

<div class="app">
  <div class="card">
    <h3>Tracking Order</h3>
    <p><b><?= $orderId ?></b></p>
    <span class="status">Out for Delivery</span>

    <ul class="progress">
      <li>✔ Order Placed</li>
      <li>✔ Shipped</li>
      <li>🚚 Out for Delivery</li>
      <li>⬜ Delivered</li>
    </ul>

    <a class="btn gray" href="index.php">Back</a>
  </div>
</div>

</body>
</html>
