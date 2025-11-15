/// Referenced file - TypeScript from script.ts > script.js

function pass(length: number = 12): string {
    const char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!@#$%^&*()";
    let password = "";
    for(let i = 0; i < length; i++){
        const ind = Math.floor(Math.random() * char.length);
        password += char[ind];
    }
    return password;
}

const btn = document.getElementById("gen") as HTMLButtonElement;
const  inp = document.getElementById("password") as HTMLInputElement;
const passLen = document.getElementById("char-qty") as HTMLInputElement;
const vis = document.getElementById("see") as HTMLButtonElement;

btn.addEventListener("click", () => {
    let length = parseInt(passLen.value, 10);

    if (length > 20) length = 20;
    if (length < 6) length = 6;

    const password = pass(length);
    inp.value = password;

    inp.type = "password";
});

vis.addEventListener("click", () => {
    if (inp.type == 'password'){
        inp.type = 'text';
        vis.textContent = "Hide Password";
    }
    else{
        inp.type = 'password';
        vis.textContent = "Show Password";
    }
});


