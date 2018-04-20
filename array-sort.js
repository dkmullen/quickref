/*jshint esversion: 6 */

// Add an object into an already sorted array of objects
let myArr = [
  {name: "Brad", age: 51},
  {name: "Dennis", age: 53},
  {name: "Jeff", age: 55}
];
//console.log(myArr[0].name);

function add(newObj) {
  for (let item of myArr) {
    if (newObj.name < item.name) {
      myArr.splice(myArr.indexOf(item), 0, newObj);
      break;
    }
  }
  console.log(myArr);

}
// add({name: "Chuck", age: 43});

// Add objects one at a time, in order, to an array.
let myArr2 = [];

function add2(newObj) {
  if (myArr2.length === 0) {
    myArr2.push(newObj);
  } else {
    for (let item of myArr2) {
      if (newObj.name < item.name) {
        myArr2.splice(myArr2.indexOf(item), 0, newObj);
        break;
      }
    }
  }
  console.log(myArr2);
}
add2({name: "Jeff", age: 55});
add2({name: "Brad", age: 51});
add2({name: "Dennis", age: 53});
add({name: "Chuck", age: 43});

// Sort an array of objects by name
let myArr3 = [
  {name: "Jeff", age: 55},
  {name: "Brad", age: 51},
  {name: 'Alfred', age: 26},
  {name: 'Zander', age: 41},
  {name: "Dennis", age: 53},
];

function compare(a, b) {
  if (a.name > b.name) {
    comparison = 1;
  } else if (a.name < b.name) {
    comparison = -1;
  }
  return comparison;
}
//console.log(myArr3.sort(compare));
