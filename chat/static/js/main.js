(function ($) {
    $(function () {
        // console.log('Ready to go!');

        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
     $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax('/api/message/', {
        'error': function (response, error) {
            console.log('Error Found');
            // $('body').html('You broke the server');
                console.log(error, response);
        },
        'success':function(data) {
            console.log('data', data);

            data.forEach(showMessageItem);
        }
    });

    function showMessageItem(Message.text){
      $('#message_container').append('<p>' + Message.text + '</p>');
    }

    $('#add-text-form').on('submit', function(event){
        event.preventDefault();

        var messageTypedIn = $('#messages').val();
        var user = localStorage.getItem('logged_in_user');
        console.log(messageTypedIn);

        $.ajax('/api/message/', {
        'method': 'POST',
        'data': {'text': messageTypedIn},
        'success': function (data) {
          console.log('success!');
          showMessageItem(data);
        },
        'error': function(){
        }
      });
        showMessageItem(data);
        console.log('Add Message')
    });



    });

}(jQuery));