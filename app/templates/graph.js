let xhr = new XMLHttpRequest();
xhr.open('GET', '/getDataGraph');
xhr.send();
var paramsString = document.location.href.split("/");
console.log(paramsString[paramsString.length-1]);


xhr.onload = function() {
  let arr = [];
  arr.push(xhr.response);
  
    var ctx = document.getElementById("myChart").getContext("2d");
      var myChart = new Chart(ctx, {
        type: "line",
        data: {
          labels: [
            "12.00",
            "13.00",
            "14.00",
            "15.00",
            "16.00",
            "17.00",
            "18.00",
          ],
          datasets: [
            {
              label: "Температура, °C",
              data: arr,
              backgroundColor: "rgba(153,205,1,0.6)",
            },
            {
              label: "Влажность, %",
              data: [2, 2, 5, 5, 2, 1, 10],
              backgroundColor: "rgba(155,153,10,0.6)",
            },
          ],
        },
      });
    };
// [2, 20, 3, 17, 6, 3, 7]