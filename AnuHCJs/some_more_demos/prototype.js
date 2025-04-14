var Arithmetic = /** @class */ (function () {
  function Arithmetic(num1, num2) {
    this.num1 = num1;

    this.num2 = num2;
  }

  Arithmetic.prototype.addition = function () {
    console.log("Addition: " + (this.num1 + this.num2));
  };

  Arithmetic.prototype.sub = function () {
    console.log("Sub:" + (this.num1 - this.num2));
  };

  Arithmetic.prototype.mul = function () {
    console.log("Mul: " + this.num1 * this.num2);
  };

  Arithmetic.prototype.div = function () {
    console.log("division: " + this.num1 / this.num2);
  };

  return Arithmetic;
})();

var demo = new Arithmetic(50, 20);

demo.addition();

demo.sub();

demo.mul();

demo.div();
