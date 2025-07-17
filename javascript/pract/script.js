const PI = 3.14159;
let radius;
let circumference;

document.getElementById('myButton').onclick = function() {
    radius = document.getElementById("radius").value;
    radius = Number(radius);
    // document.getElementById("h3").textContent = "The radius is: "  + radius + " units";
    circumference = 2 * PI * radius;
    document.getElementById("result").textContent = circumference;
}



