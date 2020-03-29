/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
class Polygon {
    constructor(heights) { //Constructor of Polygon class will be called each time object created.
        var polygon_perimeter = 0; //initialise the variable where perimeter will be stored
        for (var index in heights){
            polygon_perimeter += heights[index]; //calculating perimeter
        }
        this.my_perimeter = polygon_perimeter; //this refers to owner's object
    }
    
     perimeter() {
        return this.my_perimeter; //each time when perimeter() method is being called, the value of polygon_perimeter will be returned by this.my_perimeter.
    }
    
}

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());