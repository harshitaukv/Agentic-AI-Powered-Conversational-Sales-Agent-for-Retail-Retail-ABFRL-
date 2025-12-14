<?php
session_start();
$orderId = $_SESSION['order_id'] ?? 'Unknown Order';
?>

<!DOCTYPE html>
<html>
<head>
<title>Support Chat</title>
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>

<div class="navbar">Chat • <?= $orderId ?></div>

<div class="app">
  <div class="card">
    <div class="chatbox" id="chatBox">
      <div class="bot">Hi! I'm assisting you with <?= $orderId ?>.</div>
    </div>

    <input id="chatInput" placeholder="Type your message">
    <a class="btn" onclick="sendMessage()">Send</a>
    <a class="btn gray" href="index.php">Back</a>
  </div>
</div>

<script src="./assets/app.js"></script>
</body>
</html>
