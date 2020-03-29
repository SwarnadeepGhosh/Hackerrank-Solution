'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    // Write your code here
    var arr1= ['a','e','i','o','u'];
    var arr2=['b','c','d','f','g'];
    var arr3=['h','j','k','l','m'];
    var arr4=['n','p','q','r','s','t','v','w','x','y','z'];
    if(arr1.indexOf(s[0])>=0)
        letter='A';
    else if(arr2.indexOf(s[0])>=0)
        letter='B';
    else if(arr3.indexOf(s[0])>=0)
        letter='C';
    else if(arr4.indexOf(s[0])>=0)
        letter='D';
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}