<?php
session_start();
$orderId = $_SESSION['order_id'] ?? 'Unknown Order';
?>

<!DOCTYPE html>
<html>
<head>
<title>Confirmation</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">Confirmation</div>

<div class="app">
  <div class="card">
    <h3>Request Submitted</h3>
    <p>Order: <b><?= $orderId ?></b></p>

    <a class="btn" href="index.php">Back to Dashboard</a>
  </div>
</div>

</body>
</html>
