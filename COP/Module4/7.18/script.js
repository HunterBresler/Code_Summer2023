function divideArray(nums){
    nums.sort(function(a, b){return a-b});
    let even = [];
    let odd = [];
    nums.forEach(element => {
        if (element % 2 == 1){
            odd.push(element);
        }
        else if (element % 2 == 0){
            even.push(element);
        }
    });
    console.log('Even numbers:')
    if (even.length == 0){
        console.log('None');
    }
    even.forEach(element => {
        console.log(element);
    });
    console.log('Odd numbers:')
    if (odd.length == 0){
        console.log('None');
    }
    odd.forEach(element => {
        console.log(element);
    });
}    
