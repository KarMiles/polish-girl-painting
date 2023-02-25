// Message timeout
setTimeout(function () {
    var messages = document.getElementById('msg');
    var alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);