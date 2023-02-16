// menu-container
// menu-button

const menuButton = document.getElementById('menu-button')
const menuContainer = document.getElementById('menu-container')

menuButton.addEventListener('click',function(){
    menuContainer.classList.toggle('hidden')
})
