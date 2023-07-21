window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
   let cI = parseFloat(document.querySelectorAll("#cInput"));
   let fI = parseFloat(document.querySelectorAll("#fInput"));
   let conversion = 0;
   const conv = document.getElementById("convertButton");
   
   conv.addEventListener("click", function(){if(cI){conversion = convertCtoF(cI)}else if(fI){conversion = convertFtoC(fI)}});
}

function convertCtoF(degreesCelsius) {
   return degreesCelsius*(9/5) + 32;
}

function convertFtoC(degreesFahrenheit) {
   return (degreesFahrenheit-32)*(5/9);
}
