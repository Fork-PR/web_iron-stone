document.addEventListener("DOMContentLoaded", getLocalStorage);

function getLocalStorage() {
  const storedUser = JSON.parse(localStorage.getItem("user"));
  displayAuth(storedUser.id, storedUser.pw);
}

function displayAuth(username, password) {
  const id = document.getElementById("id");
  const pw = document.getElementById("password");
  id.innerText = username;
  pw.innerText = password;
}