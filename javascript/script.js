// console.log('Hello bro');
// console.log('i like pizza');
// window.alert('this is an alert');

// document.getElementById('h1').textContent = 'Hello By ID'
// document.getElementById('P').textContent = 'P Tag By ID'
//  let x;
//  let y;

//  x = 1000;
//  y = 2000;

//  let name;
//  name = 'John';
//  let z = x + y;

//  console.log(z);

//  console.log(typeof z);dasda

//  console.log( `give me ${z} rupees`);

//  console.log( `give me $${x*y} rupees`);

//  console.log( `give me %${x*y} rupees`);

//  console.log( `give me ${name} rupees`);

//  console.log(typeof name);

//  let online = true;

//  console.log(typeof online);
//  console.log(`he is online: \n${online}`);

// //  console.log(``)

// // let username;
// // let password;

// // username= window.prompt("whats your username");
// // console.log(username);
// username = window.prompt("Enter your username");

// console.log(username);

// username = 11212

// console.log(username)

let username;

document.getElementById("MySubmit").onclick = function(){
    username = document.getElementById("Input").value;
    console.log(username);
    document.getElementById("h1").textContent =`Hello ${username}`
}