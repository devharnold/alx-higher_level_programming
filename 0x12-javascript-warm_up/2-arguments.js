#!/usr/bin/node

if(Process.argv.length > 3){
    console.log('Arguments found');
} else if (process.argv.length === 3) {
    console.log('Argument found');
}else{
    console.log('No argument');
}