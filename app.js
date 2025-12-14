function sendMessage(){
  const input=document.getElementById("chatInput");
  const chat=document.getElementById("chatBox");
  if(input.value==="") return;

  const user=document.createElement("div");
  user.className="user";
  user.innerText=input.value;
  chat.appendChild(user);

  input.value="";

  setTimeout(()=>{
    const bot=document.createElement("div");
    bot.className="bot";
    bot.innerText="Thanks for reaching out. Our agent is reviewing your request.";
    chat.appendChild(bot);
    chat.scrollTop=chat.scrollHeight;
  },1000);
}

function selectFeedback(el){
  document.querySelectorAll(".feedback span")
    .forEach(e=>e.style.opacity="0.3");
  el.style.opacity="1";
  alert("Thank you for your feedback!");
}
