document.addEventListener("DOMContentLoaded", function () {
  fetch("http://127.0.0.1:8000/bobapps/menuList")
    .then((response) => response.json())
    .then((data) => getMenuList(data))
    .catch((error) =>
      console.error("데이터를 불러오는 중 오류가 발생했습니다:", error)
    );
});

function getMenuList(data) {
  data.menu.forEach((item) => {
    menu_type = item.menu_course_type;
    const container = document.getElementById(menu_type);
    const menu_list = setMenu(item.set_menu_name);
    container.appendChild(menu_list);
  });
}

function setMenu(data) {
  const container = document.createElement("div");
  data.forEach((menu) => {
    const listItem = document.createElement("li");
    const spanElement = document.createElement("span");
    spanElement.classList.add("menu-text");
    spanElement.innerText = menu;
    listItem.appendChild(spanElement);

    container.appendChild(listItem);
  });

  return container;
}

document
  .getElementById("login-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch("http://127.0.0.1:8000/bobapps/login/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          const info = { id: data.username, pw: data.password };
          localStorage.setItem("user", JSON.stringify(info));
          window.location.href = `http://127.0.0.1:8000/bobapps/loginPage/`;
        } else {
          const failMessage = document.getElementById('fail-message');
          failMessage.innerText = data.message
          console.log("Login failed");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });