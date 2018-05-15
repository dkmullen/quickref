// sort

let sorting = ['Biff', 'Sadie11', 'Gretchen', 'Gabe', 'Diesel', 'Sadie7', 'Tiny Rick'];
let dogs2 = [
  { dog: 'Biff', age: 11 },
  { dog: 'Tiny Rick', age: 4 },
  { dog: 'Gabe', age: 2 },
  { dog: 'Sadie11', age: 11 },
  { dog: 'Gretchen', age: 3 },
  { dog: 'Sadie7', age: 7 },
];

function mapOrder (array, order, key) {
  
  array.sort( function (a, b) {
    var A = a[key], B = b[key];
    
    if (order.indexOf(A) > order.indexOf(B)) {
      return 1;
    } else {
      return -1;
    }
    
  });
  
  console.log(array);
};

mapOrder(dogs2, sorting, "dog");