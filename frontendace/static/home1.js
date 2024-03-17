const sidebar = document.querySelector(".sidebar");
const sidebarClose = document.querySelector("#sidebar-close");
const menu = document.querySelector(".menu-content");
const menuItems = document.querySelectorAll(".submenu-item");
const subMenuTitles = document.querySelectorAll(".submenu .menu-title");
const oneSelector  = document.getElementById("oneSelector");
const twoSelector = document.getElementById("twoSelector");
const form1 = document.getElementById("one");
const form2 = document.getElementById("two");

if (window.innerWidth <800) {
  sidebar.classList.toggle("close");
}


sidebarClose.addEventListener("click", () => 
  sidebar.classList.toggle("close")
);
let oneActive = true;
let twoActive = false;

menuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    menu.classList.add("submenu-active");
    item.classList.add("show-submenu");
    menuItems.forEach((item2, index2) => {
      if (index !== index2) {
        item2.classList.remove("show-submenu");
      }
    });
  });
});

subMenuTitles.forEach((title) => {
  title.addEventListener("click", () => {
    menu.classList.remove("submenu-active");
  });
});

function toggler() {
  oneActive =!oneActive;
  twoActive =!twoActive;
  if (oneActive === true) {
    form1.style.display = 'flex'
    oneSelector.className = 'optionOne active'
    twoSelector.className = 'optionTwo'
    form2.style.display = 'none';
  }
  if (twoActive) {
    form2.style.display = 'flex'
    form1.style.display = 'none';
    oneSelector.className = 'optionOne'
    twoSelector.className = 'optionTwo active'
  }
}