function student(name, qual) {
    this.name = name;
    this.qual = qual;
}
student.prototype.age = 22;

var stud1 = new student('daniel', 'BCA');
console.log(stud1.age);
console.log(stud1.name);
console.log(stud1.qual);
var myfun1 = function show() {
    console.log("Its a function expression");
}
var myfun2 = function () {
    console.log("Its anonymous function");
};
var myfun3 = () => {
    console.log("Its an arrow function");
};

myfun1();
myfun2();
myfun3();

var demo1 = (a, b) => {
    console.log(a + " " + b);
};
demo1(100, 200);
var demo2 = (a, b, c) => { 
    console.log("addition: "+(a+b+c)); 
    console.log("substraction: "+(c-b-a));
    console.log("multiplication: "+(a*b*c));
    console.log("Division: "+c/(a+b));
     };
demo2(100, 200, 300);


var emp1 = (id=101,salary,age=22,address)=> {  
    console.log("Employee id:" + id);
    console.log("Employee salary: "+salary);  
    console.log("Employee age:"+ age); console.log("Employee address:"+address);
    }
emp1(emp1.id,20000.00,emp1.age, 'hydrabad');