function register()
{
  name=document.querySelector('#name').value;
  if(!Boolean(name) || name==="undefined")
  {
    alert("retry");
    return true;
  }
  localStorage.name=name;
  location.replace("/chatroom");
}

function welcome()
{

  if(!localStorage.name){
    reg_form='<form><input id="name" name="name" type="text" class="form-control" placeholder="User Name"><br><button onclick="register()">Register</button></form>';
    document.querySelector('#reg_form').innerHTML=reg_form;
  }
  else {
    window.location.href = '/chatroom';
  }
}
