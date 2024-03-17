const menu = document.getElementById('menu');
const navOptions = document.getElementById('navOptions');

let isNavActive = false;
function navToggler() {
    isNavActive = !isNavActive
    if (isNavActive === false)  {
        menu.innerHTML = '<i class="fa fa-bars"></i>';
        navOptions.className = 'navOptions'
    }else if (isNavActive === true) {
        menu.innerHTML = '<i class="fa fa-times"></i>';
        navOptions.className = 'navOptions navComes'
    }
}