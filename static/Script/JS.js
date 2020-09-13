let backdrop=document.getElementById("backdrop");
let cont7=document.getElementById("container7");
let cont73=document.getElementById("container73");




function Toggle_Backdrop()
{
  backdrop.classList.toggle("visible");
};

function Toggle_LoginForm()
{
  cont7.classList.toggle("visible");
  Toggle_Backdrop();
};

function Toggle_adminForm()
{
  cont73.classList.toggle("visible");
  Toggle_Backdrop();
};


