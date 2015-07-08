console.log("HERE");
function goog_signin_cb (auth_res) {
  console.log("THERE");
  if (auth_res['code']) {
    $('#sign-up-in').attr('style', 'display: none');
    if (auth_res['error']) {
      $('#result').html(
        "Authorization error, see console"
      );
      console.log("there was an error: " + auth_res['error']);
    } else {
      $.ajax({
        type: 'POST',
        url: '/gconnect?state='+STATE,
        processData: false,
        contentType: 'application/octet-stream; charset=utf-8',
        data: auth_res['code'],
        success: function(result) {
          if (result) {
            $('#result').html('Login Successful</br>' +
                              result + '</br>Redirecting...');
            setTimeout(function () {
              window.location.href = "/";
            }, 4000);
          } else {
            $('#result').html(
              "Failed to make a server-side call."
            );
          }
        },
        error: function(jqXHR, textStatus, errorThrown) {
          $('#result').html(
            "Failed to make a server-side call.  "+
              "Check your configuration and console."
          );
          console.log("there was an error: " + errorThrown);
        }
      });
    }
  }
}
