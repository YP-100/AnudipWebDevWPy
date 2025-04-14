
let name, division;
({ name, division } = { name: 'Anil', division: 'first' });

console.log(name);
console.log(division);

const stud1 = {
  fname: 'Akshay',
  Iname: 'kumar',
  rollno: '121',
  result: 'pass',
  division: 'first'
};

const stud2 = stud1;

console.log(stud2);


function average(...args) {
  console.log(args);
  const avg = args.reduce(function (a, b) {
    return a + b;
  });
  const result = avg / args.length;
  return result;
}

console.log("Average is: " + average(1, 2, 3, 4, 5, 6));


const employee = {
  empname: 'amar',
  empcode: 3333,
  empsalary: 8000.00
};

console.log(employee.empname);
console.log(employee.empcode);
console.log(employee.empsalary);
