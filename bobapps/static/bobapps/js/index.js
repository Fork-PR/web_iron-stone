document
.getElementById("login-form")
.addEventListener("submit", handleLoginForm);

document.addEventListener("DOMContentLoaded", handleMenuList);

function handleLoginForm(event) {
  event.preventDefault();
  const formData = new FormData(this);
  fetch("http://127.0.0.1:8000/bobapps/user_login/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        const info = { id: data.username, pw: data.password };
        localStorage.setItem("user", JSON.stringify(info));
        window.location.href = `http://127.0.0.1:8000/bobapps/login_page/`;
      } else {
        const failMessage = document.getElementById('fail-message');
        failMessage.innerText = data.message
        console.log("Login failed");
      }
    })
    .catch((error) => {
      const failMessage = document.getElementById('fail-message');
      failMessage.innerText = data.message
      console.error("Error:", error);
    });
}

function handleMenuList() {
  fetch(`http://127.0.0.1:8000/bobapps/menuList?date=${getCurDate()}`, {
    method: 'GET',
  })
  .then((response) => response.json())
  .then((data) => getMenuList(data))
  .catch((error) =>
      console.error("데이터를 불러오는 중 오류가 발생했습니다:", error)
    );
}

function getMenuList(data) {
  data.menu_data.forEach((item) => {
    console.log(item)
    const menu_type = item.menu_course_type;
    const container = document.getElementById(menu_type);
    // const menu_list = setMenu(item);
    // container.appendChild(menu_list);
    const div = document.createElement("div");
    div.appendChild(setMenu(item.main_dish));
    item.sub_menus.forEach((menu) => {
      div.appendChild(setMenu(menu));
    })
    // div.appendChild(listItem);
    // container.setMenu(menu);
    container.appendChild(div);
  });
}

function setMenu(data) {
  const listItem = document.createElement("li");
  const spanElement = document.createElement("span");
  spanElement.classList.add("menu-text");
  spanElement.innerText = data;
  listItem.appendChild(spanElement);
  return listItem;
}

function getCurDate(){
  const currentDate = new Date()
  const year = currentDate.getFullYear();
  const month = String(currentDate.getMonth() + 1).padStart(2, '0');
  const day = String(currentDate.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`
}
