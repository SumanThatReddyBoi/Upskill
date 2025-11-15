/// Referenced file - TypeScript from script.ts > script.js
function pass(length) {
    if (length === void 0) { length = 12; }
    var char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!@#$%^&*()";
    var password = "";
    for (var i = 0; i < length; i++) {
        var ind = Math.floor(Math.random() * char.length);
        password += char[ind];
    }
    return password;
}
var btn = document.getElementById("gen");
var inp = document.getElementById("password");
var passLen = document.getElementById("char-qty");
var vis = document.getElementById("see");
btn.addEventListener("click", function () {
    var length = parseInt(passLen.value, 10);
    if (length > 20)
        length = 20;
    if (length < 6)
        length = 6;
    var password = pass(length);
    inp.value = password;
    inp.type = "password";
});
vis.addEventListener("click", function () {
    if (inp.type == 'password') {
        inp.type = 'text';
        vis.textContent = "Hide Password";
    }
    else {
        inp.type = 'password';
        vis.textContent = "Show Password";
    }
});
