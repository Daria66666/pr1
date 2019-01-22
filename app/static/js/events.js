$(document).ready(function(){
    $('#addtransaction').click(function(e){
        alert("Вы собираетесь добавить транзакцию")
    })
    $('#logout').click(function(e){
        alert("Вы уверены, что хотите покинуть страницу?")
    })
    $('#submitbutton').click(function(e){
        login = $('#login').val()
        if (login.length<3||login.length>20||login.indexOf(' ')!=-1||login.indexOf(':')!=-1||login.indexOf(',')!=-1||login.indexOf('.')!=-1){
        alert('Логин должен быть 3-20 символов длиной, может содержать только a-z,A-Z,0-9 и не должен содержать пробелы');
        e.preventDefault()}
        password = $('#password').val()
        if (password.length<3||password.length>20||password.indexOf(' ')!=-1||password.indexOf(':')!=-1||password.indexOf(',')!=-1||password.indexOf('.')!=-1){
        alert('Пароль должен быть 6-20 символов длиной, может содержать только a-z,A-Z,0-9 и не должен содержать пробелы');
        e.preventDefault()}
        email = $('#email').val()
        if (email.indexOf('@')==-1||email.indexOf('.')==-1){
        alert('Введите правильный email');
        e.preventDefault()}
        $.post(
             "notuniqlogin",
            function(response){if (response){ alert('Такой логин занят')}
    })
        $('#loginbutton').click(function(e) {
            username = $('#username').val()
            if (username.length < 3 || username.length > 20 || username.indexOf(' ') != -1 || username.indexOf(':') != -1 || username.indexOf(',') != -1 || username.indexOf('.') != -1) {
                alert('Логин должен быть 3-20 символов длиной, может содержать только a-z,A-Z,0-9 и не должен содержать пробелы');
                e.preventDefault()
            }
            password = $('#password').val()
            if (password.length < 3 || password.length > 20 || password.indexOf(' ') != -1 || password.indexOf(':') != -1 || password.indexOf(',') != -1 || password.indexOf('.') != -1) {
                alert('Пароль должен быть 6-20 символов длиной, может содержать только a-z,A-Z,0-9 и не должен содержать пробелы');
                e.preventDefault()
            }
        })
     $('#somebutton').click(function(e){
         $.post(
             "ajax_path",
            function(response){alert(response.message)})
    })
})

