let button_Click = document.querySelector("#log_guest");

let guestLogin = () => {
    let username = document.querySelector('#username');
    let password = document.querySelector('#password');

    username.value = "guest";
    password.value = "gggg1234";
}


button_Click.addEventListener("click", guestLogin);