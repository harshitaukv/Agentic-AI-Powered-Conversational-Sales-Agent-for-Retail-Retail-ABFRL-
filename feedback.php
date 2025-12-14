<?php
session_start();
$orderId = $_SESSION['order_id'] ?? 'Unknown Order';
?>

<!DOCTYPE html>
<html>
<head>
<title>Feedback</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">Feedback • <?= $orderId ?></div>

<div class="app">
  <div class="card">
    <h3>Rate Your Experience</h3>

    <div class="feedback">
      <span onclick="selectFeedback(this)">😊</span>
      <span onclick="selectFeedback(this)">😐</span>
      <span onclick="selectFeedback(this)">😞</span>
    </div>

    <a class="btn secondary" href="confirmation.php">Submit</a>
  </div>
</div>

<script src="./assets/app.js"></script>
</body>
</html>
