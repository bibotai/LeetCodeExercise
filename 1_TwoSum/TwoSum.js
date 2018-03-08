
function twoSum1(nums,target){
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[j]===target-nums[i]) {
        return [i,j];
      }
    }  
  }
}




function twoSum2(nums,target){
  let result=[];
  nums.forEach((num,index) => {
    let diff=target-num;
    let k=nums.indexOf(diff);
    if (k > -1 && k !== index) {
      result=[k,index]
      return true
   }
  });
  return result;
}


//test

let nums = [2, 7, 11, 15];
let target = 9;

console.log(twoSum1(nums,target));
console.log(twoSum2(nums,target));



