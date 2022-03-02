const personPrototype = {
  greet() {
    console.log("hello!");
  },
};

const carl = Object.create(personPrototype);
carl.greet(); // hello!
a = 3;
b = 5;
if (a > b) {
  console.log("cool");
} else if (b > a) {
  console.log("not cool");
}
