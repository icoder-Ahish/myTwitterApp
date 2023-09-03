//  Closures gives you access to an outer functions scope from an inner function

// This is also look like closurs but

//  In simple words, the closure remembers the variables from the place where it is defined, no matter where it is executed.

console.log("This is simple clouser example that very similar to lexical scope and clousers ");

function oldouter (){
    var name = "Ashish";

    function oldinner(){
        console.log(`My name is ${name} \n`);
    }
    oldinner();
}
oldouter();

console.log("This is actual clouser example where variable still persist even the outer scope ");

function outer (){
    var name = "Ashish";

    function inner(){
        console.log(`My name is ${name}`);
    }
     return inner;
}
const inner  = outer();
// console.log(outer)

inner();