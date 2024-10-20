document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.messages .message');

    messages.forEach(message => {
        message.classList.add('slide-in');
    });
});
