class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is not a positive integer or equal to 0
      Object.defineProperty(this, 'width', {
        enumerable: false,
        writable: true
      });

      Object.defineProperty(this, 'height', {
        enumerable: false,
        writable: true
      });
    }
  }
}

module.exports = Rectangle;
