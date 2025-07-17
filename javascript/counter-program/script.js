const decbtn = document.getElementById("decrement");
const incbtn = document.getElementById("increment");
const resbtn = document.getElementById("reset");
const countDisplay = document.getElementById("Count");

let count = 0;

incbtn.onclick = function() {
    count++;
    countDisplay.textContent = count;
}

decbtn.onclick = function() {
    count--;
    countDisplay.textContent = count;
}

resbtn.onclick = function() {
    count = 0;
    countDisplay.textContent = count;
}
