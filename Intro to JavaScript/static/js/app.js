// from data.js
var tableData = data;

var tbody = d3.select("tbody");

tableData.forEach((ufoData) => {
    var row = tbody.append("tr");
    Object.entries(ufoData).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });

var submit = d3.select("#filter-btn");

submit.on("click", function() {
    d3.event.preventDefault();
    var input = d3.select("#datetime")
    var inputValue = input.node().value;
    console.log(inputValue);
    $("tbody").children().remove();
    var filteredData = tableData.filter(ufoSighting => ufoSighting.datetime === inputValue);
    console.log(filteredData);

    filteredData.forEach((ufoData) => {
        var row = tbody.append("tr");
        Object.entries(ufoData).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
      });

});

