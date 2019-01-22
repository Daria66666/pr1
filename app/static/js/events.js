$(document).ready(function(){
    $('#addtransaction').click(function(e){
        alert("Вы собираетесь добавить транзакцию")
    })
    $('#logout').click(function(e){
        alert("Вы уверены, что хотите покинуть страницу?")
    })
    $('#submitbutton').click(function(e){
        login = $('#login').val()
        if (login.length<3||login.length>20||length.indexOf(' ')!=-1||length.indexOf(':')!=-1||length.indexOf(',')!=-1||length.indexOf('.')!=-1){
        alert($('#login').val());
        alert('Логин должен быть 3-20 символов длиной, может содержать только a-z,A-Z,0-9 и не должен содержать пробелы');}
        password = $('#password').val()
        if (password.length<3||password.length>20||password.indexOf(' ')!=-1||password.indexOf(':')!=-1||password.indexOf(',')!=-1||password.indexOf('.')!=-1){
        alert($('#password').val());
        alert('Пароль должен быть 6-20 символов длиной, может содержать только a-z,A-Z,0-9 и не должен содержать пробелы');}
        email = $('#email').val()
        if (email.indexOf('@')==-1||email.indexOf('.')==-1){
        alert($('#email').val());
        alert('Введите правильный email')}
    })
        e.preventDefault()
});