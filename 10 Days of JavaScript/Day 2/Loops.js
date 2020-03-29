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

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var len=s.length,i=0;
    var consArray=[];
    for(i=0;i<len;i++){
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u'){
            console.log(s[i]);
        }
        else{
            consArray.push(s[i]); // pushing element to new consonant array
        }
    }
    for(i=0;i<consArray.length;i++){
       console.log(consArray[i]);
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}