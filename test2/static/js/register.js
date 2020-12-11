$(document).ready(function()
{
$('.pwd').keyup(function()
{
$('#strength_message').html(checkStrength($('.password').val()))
})
function checkStrength(password)
{

var strength = 0
if (password.length <= 0) {
$('#strength_message').removeClass()
$('#strength_message').addClass('short')
return ''
}

if (password.length < 6) {
$('#strength_message').removeClass()
$('#strength_message').addClass('short')
return 'Too short'
}

if (password.length > 7) strength += 1
if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/))  strength += 1
if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/))  strength += 1
if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/))  strength += 1
if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1
if (strength < 2 )
{
$('#strength_message').removeClass()
$('#strength_message').addClass('weak')
return 'Minimum 8 charactors including special charactors'
}
else if (strength == 2 )
{
$('#strength_message').removeClass()
$('#strength_message').addClass('good')
return 'Good'
}
else
{
$('#strength_message').removeClass()
$('#strength_message').addClass('strong')
return 'Strong'
}
}
});

$(".pwd").mouseenter(function(){
    $('#strength_message').show();
    
    });
    
    $(".pwd").mouseleave(function(){
    $('#strength_message').hide();
});

$('.cpassword').keyup(function(){
    cps=$(this).val();
    pass=$('.pwd').val()


    if (cps == pass)
    {
      $(this).css("border", "2px solid green");
      $('.pswdconfirm_message').hide()
    }
    else
    {
      $(this).css("border", "5px black");
      $('.pswdconfirm_message').html(' Incorrect password')
    }


});

