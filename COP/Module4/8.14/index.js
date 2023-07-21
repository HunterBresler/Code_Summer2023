function parseScores(scoresString) {
   return scoresString.split(' ');
}

function buildDistributionArray(scoresArray) {
   let scores = [0, 0, 0, 0, 0]
   scoresArray.forEach(element => {
      if (element >= 90){
         scores[0]++;
      }
      else if (element >= 80){
         scores[1]++;
      }
      else if (element >= 70){
         scores[2]++;
      }
      else if (element >= 60){
         scores[3]++;
      }
      else{
         scores[4]++;
      }
   });
   return scores;
}

function setTableContent(userInput) {
   let content = parseScores(userInput);
   let grades = buildDistributionArray(content);

   graph = document.getElementById("firstRow");
   graph.innerHTML += '<td><div style="height:'+10*grades[0]+'px" class="bar0"></div></td>';
   graph.innerHTML += '<td><div style="height:'+10*grades[1]+'px" class="bar1"></div></td>';
   graph.innerHTML += '<td><div style="height:'+10*grades[2]+'px" class="bar2"></div></td>';
   graph.innerHTML += '<td><div style="height:'+10*grades[3]+'px" class="bar3"></div></td>';
   graph.innerHTML += '<td><div style="height:'+10*grades[4]+'px" class="bar4"></div></td>';

   scores = document.getElementById("thirdRow");
   scores.innerHTML += '<td><div>'+grades[0]+'</div></td>';
   scores.innerHTML += '<td><div>'+grades[1]+'</div></td>';
   scores.innerHTML += '<td><div>'+grades[2]+'</div></td>';
   scores.innerHTML += '<td><div>'+grades[3]+'</div></td>';
   scores.innerHTML += '<td><div>'+grades[4]+'</div></td>';
}

// The argument can be changed for testing purposes
setTableContent("45 78 98 83 86 99 90 59");