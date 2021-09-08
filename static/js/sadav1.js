
function getInputValue(){
    var inputValue1="your details is stored";
      alert(inputValue1);
}
function friend()
{
    var suscribe="thanks for suscribe our institute";
    alert(suscribe);
}
burger=document.querySelector('.burger')
navbar=document.querySelector('.navbar')
navlist=document.querySelector('.nav-list')
rightnav=document.querySelector('.rightNav')


burger.addEventListener('click',()=>{
    rightnav.classList.toggle('v-class');
    navlist.classList.toggle('v-class');
    navbar.classList.toggle('h-nav');
})