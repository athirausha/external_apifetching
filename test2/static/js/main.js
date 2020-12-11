

// function messages(messages, clr)
// {
//     $.notify({
//         message: "<strong>"+messages+"</strong>"
//     },
//     {
//         type: clr
//     });
// }

// CAPTCHA
var code;
function createCaptcha() {
  //clear the contents of captcha div first 
  document.getElementById('captcha').innerHTML = "";
  var charsArray =
  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%^&*";
  var lengthOtp = 6;
  var captcha = [];
  for (var i = 0; i < lengthOtp; i++) {
    //below code will not allow Repetition of Characters
    var index = Math.floor(Math.random() * charsArray.length + 1); //get the next character from the array
    if (captcha.indexOf(charsArray[index]) == -1)
      captcha.push(charsArray[index]);
    else i--;
  }
  var canv = document.createElement("canvas");
  canv.id = "captcha";
  canv.width = 100;
  canv.height = 50;
  var ctx = canv.getContext("2d");
  ctx.font = "25px Georgia";
  ctx.strokeText(captcha.join(""), 0, 30);
  //storing captcha so that can validate you can save it somewhere else according to your specific requirements
  code = captcha.join("");
  document.getElementById("captcha").appendChild(canv); // adds the canvas to the body element
}
  
$('#cpatchaTextBox').keyup(function(){
  cps=$(this).val();
  


  if (cps == code)
  {
    
    $('.captcha_message').hide()
  }
  else
  {
  
    $('.captcha_message').html(' Invalid Captcha. try Again')
  }


});



    
      
             $(function() {
               $("form[name='Login']").validate({
                 rules: {
                   
                   email: {
                     required: true,
                     email: true
                   },
                   password: {
                     required: true,
                     
                   }
                 },
                  messages: {
                   email: "Please enter a valid email address",
                  
                   password: {
                     required: "Please enter password",
                    
                   }
                   
                 },
                 submitHandler: function(form) {
                   form.submit();
                 }
               });
             });
             
    
    
   
  //  TO REGISTER
    $('.createaccount').click(function(){
      
        var email =$('.email').val()
        var password =$('.password').val()
        var fname =$('.fname').val()
        var mobile =$('.mobile').val()
        var cpassword =$('.cpassword').val()
        var type=$('.seltype option:selected').val()
       
        var val_captcha=$("#cpatchaTextBox").val()
        console.log(val_captcha)
        if (val_captcha == code) {
         
          $('.captcha_message').hide()
        

        $.ajax({
            type:"POST",
            url: "/register_save/",
            async:false,
            data:{csrfmiddlewaretoken: window.CSRF_TOKEN, email:email, password:password,fname:fname,seltype:type,mobile:mobile,cpassword:cpassword},
               
            success: function(data){
            console.log(data.data);
            }

            });
  // To FETCH 10 ACTIVITIES ON REGISTER

            for(i=0;i<10;i++)
            {
        $.ajax({
            type: "GET",
            url: "http://www.boredapi.com/api/activity?type="+type,
            cache: false,
            // data: dataString,
            dataType: 'JSON',
            
            
            success: function(data){
                console.log(data);
                console.log(data.activity);
                activity=data.activity;
                participants=data.participants;
                type=data.type;
                price=data.price;
                accessibility=data.accessibility
                link=data.link
               
                $.ajax({
                    type:"POST",
                    url: "/save_data/",
                    async:false,
                    data:{csrfmiddlewaretoken: window.CSRF_TOKEN,email:email, price:price, activity:activity,type:type,participants:participants,price:price,link:link,accessibility:accessibility},
                       
                    success: function(data){
                    console.log(data.data);
                    }
        
                    });
            
            
            }
            
            });
            setTimeout(function(){
                      location.reload();
                    }, 4000);
            
        }
         // To FETCH 10 ACTIVITIES ON REGISTER END
        
             
        }else{
          // alert("Invalid Captcha. try Again");
          $('.captcha_message').html(' Invalid Captcha. try Again')
          createCaptcha();
        }
        
       
        // fetch('http://www.boredapi.com/api/activity?type='+type)
        // .then(res => res.json())//response type
        // .then(data => console.log(data)); //log the data;
    });

      // REGISTER END



     //  TO ADD 2 ACTIVITIES PER DAY

    $('.adddata').click(function(){
      console.log($('.adddata').attr('id'))
     var mail=$('.adddata').attr('id')
      $.ajax({
        type:"POST",
        url: "/sel_add_data/",
        async:false,
        data:{csrfmiddlewaretoken: window.CSRF_TOKEN,email:$('.adddata').attr('id')},
           
        success: function(data){
        console.log(data.data);
        console.log(data.type);
            
        if(data.data=='permitted')
        {
         
          $.ajax({
            type: "GET",
            url: "http://www.boredapi.com/api/activity?type="+data.type,
            cache: false,
            // data: dataString,
            dataType: 'JSON',
            
            
              success: function(data){
              
                  console.log(data);
                  console.log(data.activity);
                  activity=data.activity;
                  participants=data.participants;
                  type=data.type;
                  price=data.price;
                  accessibility=data.accessibility
                  link=data.link
                
                    $.ajax({
                        type:"POST",
                        url: "/save_data/",
                        async:false,
                        data:{csrfmiddlewaretoken: window.CSRF_TOKEN,email:mail, price:price, activity:activity,type:type,participants:participants,price:price,link:link,accessibility:accessibility},
                          
                        success: function(data){
                        console.log(data.data);
                        new Noty({
                          type: 'success',
                          layout: 'topRight',
                          theme: 'metroui',
                          text: 'Activity added to your record successfully',
                          timeout: '3000',
                          progressBar: true,
                          closeWith: ['click'],
                          killer: true,
                       }).show();
            
                        }
                        
                    });
                        setTimeout(function(){
                                location.reload();
                              }, 2000);
                
               }
            
          });
        }
        else{
         
          new Noty({
            type: 'error',
            layout: 'topRight',
            theme: 'metroui',
            text: 'You crossed daily activity adding limit.. ! 🤖',
            timeout: '2000',
            progressBar: true,
            closeWith: ['click'],
            killer: true,
         }).show();
        }

        }

        });

    });


     //  TO ADD 2 ACTIVITIES PER DAY END


    //  EDIT ROW
    $('.editbtn').click(function(){
      // alert('hhhh')
      mail=$('.adddata').attr('id')
      console.log($(this).attr('id'))
      row_id=$(this).attr('id')
      if($(this).val()== 'Edit')
      {
      $('.editfield').prop('readonly', false);
      // $(this).value('attr','Update')
      $(this).closest('tr').find('td').css({'background-color':'lightblue', 'border':'none'})  
      $('.editbtn').val('Update')
      }
      else{

              activity=$('#'+ row_id).find('.activity').val(); 
              // console.log(activity)
              participants=$('#' + row_id).find('.participants').val()
              type=$('#' + row_id).find('.type').val()
              price=$('#' + row_id).find('.price').val()
              accessibility=$('#' + row_id).find('.accessibility').val()
              link=$('#' + row_id).find('.link').val()
                
                    $.ajax({
                        type:"POST",
                        url: "/update_data/",
                        async:false,
                        data:{csrfmiddlewaretoken: window.CSRF_TOKEN,row_id:row_id,price:price, activity:activity,type:type,participants:participants,price:price,link:link,accessibility:accessibility},
                          
                        success: function(data){
                        console.log(data.data);
                        new Noty({
                          type: 'success',
                          layout: 'topRight',
                          theme: 'metroui',
                          text: 'Data updated successfully',
                          timeout: '3000',
                          progressBar: true,
                          closeWith: ['click'],
                          killer: true,
                       }).show();

                        }
            
                    });
                        setTimeout(function(){
                                location.reload();
                              }, 2000);

      }



    });
     //  EDIT ROW END

    // TO DELETE ACTIVITY ON ADMIN VIEW PAGE

    $('.deletebtn').click(function(){
      row_id=$(this).attr('id')
      $.ajax({
        type:"POST",
        url: "/delete_data/",
        async:false,
        data:{csrfmiddlewaretoken: window.CSRF_TOKEN,row_id:row_id},
          
        success: function(data){
        console.log(data.data);
        new Noty({
          type: 'success',
          layout: 'topRight',
          theme: 'metroui',
          text: 'Data deleted successfully',
          timeout: '2000',
          progressBar: true,
          closeWith: ['click'],
          killer: true,
       }).show();
        }

    });
        setTimeout(function(){
                location.reload();
              }, 2000);

    })
    // TO DELETE ACTIVITY ON ADMIN VIEW PAGE END