document.addEventListener("DOMContentLoaded", function () {
  // 로컬 스토리지에 저장된 정보를 가져옴
  const storedUser = JSON.parse(localStorage.getItem("user"));
  displayAuth(storedUser.id, storedUser.pw);
});

function displayAuth(username, password) {
  const id = document.getElementById("id");
  const pw = document.getElementById("password");
  id.innerText = username;
  pw.innerText = password;
}