const loginName = document.getElementById('loginName');
const loginPassword = document.getElementById('loginPassword');
const errorSpan = document.getElementById('errorSpan');
const registerName = document.getElementById('registerName');
const registerPassword = document.getElementById('registerPassword');
const registerPasswordConfirmation = document.getElementById('registerPasswordConfirmation');
const registerEmail = document.getElementById('registerEmail');
function loginValidator(event) {
    if (loginName.value === '' || loginPassword.value === '') {
        errorSpan.innerHTML = 'Please fill in all fields';
    }
    else {
        errorSpan.innerHTML = '';
        sendData(loginName.value , loginPassword.value);
    }
    event.preventDefault();
}

function sendData(name , password) {
    console.log(name, password);
}


function signupValidator(event) {
    if (registerEmail.value === '' || registerName.value === '' || registerPassword.value === '' || registerPasswordConfirmation.value === '') {
        errorSpan.innerHTML = 'Please fill in all fields';
    }
    else if (registerPassword.value !== registerPasswordConfirmation.value) {
        errorSpan.innerHTML = 'Passwords do not match';
    }
    else {
        errorSpan.innerHTML = '';
        sendDataRegister(registerEmail.value , registerName.value , registerPassword.value);
    }
    event.preventDefault();
}

function sendDataRegister(email ,name , password) {
    console.log(email,name, password);
}