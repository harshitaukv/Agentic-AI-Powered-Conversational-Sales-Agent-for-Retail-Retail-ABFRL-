<?php
session_start();

if (isset($_POST['order_id'])) {
    $_SESSION['order_id'] = $_POST['order_id'];
}
$orderId = $_SESSION['order_id'] ?? 'Not Selected';
?>

<!DOCTYPE html>
<html>
<head>
<title>ABFRL Dashboard</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">ABFRL • Post-Purchase Experience</div>

<div class="app">
  <div class="card">

    <h3>Select Order</h3>

    <form method="post">
      <select name="order_id" style="padding:10px;width:100%;border-radius:10px;">
        <option value="ABFRL-23453">ABFRL-23453</option>
        <option value="ABFRL-87231">ABFRL-87231</option>
        <option value="ABFRL-44912">ABFRL-44912</option>
      </select>
      <button class="btn" type="submit">Load Order</button>
    </form>

    <hr>

    <p><b>Selected Order:</b> <?= $orderId ?></p>
    <span class="status">In Transit</span>

    <a class="btn" href="tracking.php">Track Package</a>
    <a class="btn danger" href="return.php">Return / Exchange</a>
    <a class="btn secondary" href="support.php">Contact Support</a>
    <a class="btn" href="feedback.php">Give Feedback</a>

  </div>
</div>

</body>
</html>
