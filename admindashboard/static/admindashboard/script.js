/**
 * Created by rabin on 16/10/16.

$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});

 */

function redirect() {
   var e = document.getElementById("usertype");
   var usrtype = e.options[e.selectedIndex].value;
   if (usrtype == 'Blogger'){
      window.location.href = "/user-dashboard/";
   }
   else if (usrtype == 'Advertiser') {
      window.location.href = "/advertiser-dashboard/";
   }
   else {
      window.location.href = "#";
   }
}