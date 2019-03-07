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

    function showMessageItem(Message){
      $('#message_container').append('<p>' + Message + '</p>');
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
        'error': function(xhr){
            console.log(xhr.statusText);
        }
      });
        // showMessageItem(data);
        console.log('Add Message')
    });

    });

}(jQuery));