setTimeout(() => {
  const message = document.querySelector(".alert");

  console.log(message)
  // 👇️ hides element (still takes up space on page)
  message.style.display = "none";
}, 3000);
