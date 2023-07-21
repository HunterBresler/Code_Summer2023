function drawTriangle(triangleSize) {

   for (let index = 0; index < triangleSize; index++) {
      let str = "*";
      for (let index2 = 0; index2 < index; index2++){
         str += "*";
      }
      console.log(str);
   }
   
}