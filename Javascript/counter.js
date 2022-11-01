let counter = 0
function count(){
   counter++;
   document.querySelector('h1').innerHTML= counter

   if (counter % 10 ===0){
    alert(`Reach at ${counter}`)//syntax in JavaScript
    // (f" Reach at {counter}") //syntax in javascript
   } 
}
document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('button').onclick = count;
});