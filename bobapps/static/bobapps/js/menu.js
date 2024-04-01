data_type = {
  date: "날짜",
  menu_type: "메뉴타입",
  main_dish: "주메뉴",
  sub_menus: "서브 메뉴",
};

document
  .getElementById("add_subMenu")
  .addEventListener("click", handleAddSubMenu);

document
  .getElementById("menu-form")
  .addEventListener("submit", handleMenuSubmit);

function handleMenuSubmit(event) {
  event.preventDefault();
  const formData = new FormData(this);

  result = [...valid_menu(formData)];
  console.log(result[0]);
  if (result[0]) {
    document.getElementById("menu-form").reset();
    fetch_menu(formData);
    return;
  }
  const el = document.querySelector(".fail-message");
  el.innerText = `지정이 안된 값이 존재합니다 (${result[1]})`;
}

function fetch_menu(formData) {
  fetch("https://web-iron-stone.vercel.app/bobapps/save_menu/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        const message = document.querySelector(".success-message");
        message.innerText = data.message;
      } else {
        const message = document.querySelector(".fail-message");
        message.innerText = data.message;
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      const message = document.querySelector(".fail-message");
      message.innerText = "데이터 저장에 실패했습니다.";
    });
}

function handleAddSubMenu(event) {
  event.preventDefault();
  const menu = document.getElementById("add-menu");
  if (menu.value == "") {
    return;
  }

  const parent = document.getElementById("add-wrap");
  const div = document.createElement("div");
  // 인풋요소
  const input = document.createElement("input");
  input.id = "sub_menus";
  input.className = "checkbox";
  input.type = "checkbox";
  input.name = "sub_menus";
  input.value = menu.value;
  input.checked = true;
  // 라벨요소
  const label = document.createElement("label");
  label.for = menu.value;
  label.innerText = menu.value;

  div.appendChild(input);
  div.appendChild(label);
  parent.appendChild(div);
  if (parent.children.length !== 1) {
    removeAttr(parent.children);
  }
  menu.value = "";
}

function valid_menu(formData) {
  const error_field = [];
  for (const entry of formData.entries()) {
    if (entry[1] == "") {
      error_field.push(data_type[entry[0]]);
    }
    console.log(entry[1]);
  }
  if (error_field.length >= 1) {
    return [false, error_field];
  }
  return [true, error_field];
}

function removeAttr(parent) {
  parent[0].children[0].removeAttribute("name");
}
