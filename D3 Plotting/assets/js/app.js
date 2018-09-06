var svgWidth = 960;
var svgHeight = 500;

// margins for the graph
var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

// width and height of the graph
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// svg container
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
.attr("transform", `translate(${margin.left}, ${margin.top})`);

var file = "data.csv"
d3.csv(file).then(successHandle, errorHandle);

function errorHandle(error) {
    throw err;
}

function successHandle(Data) {
    Data.forEach(function(data) {
        data.poverty = +data.poverty;
        data.healthcare = +data.healthcare;
    });

    // Create the X Axis Scale
    var xLinearScale = d3.scaleLinear()
        .domain([8, d3.max(Data, d => d.poverty)])
        .range([0, width]);
    
    // Create the Y Axis Scale
    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(Data, d => d.healthcare)])
        .range([height, 0]);

    // Create the X&Y axis
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);
    
    // Show the X Axis
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    // Show the Y Axis
    chartGroup.append("g")
        .call(leftAxis);

    // Create the circles for the scatterplot
    var circlesGroup = chartGroup.selectAll("circle")
        .data(Data)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d.poverty))
        .attr("cy", d => yLinearScale(d.healthcare))
        .attr("r", "15")
        .attr("fill", "blue")

    // Create Tooltips
    var toolTip = d3.tip()
    .attr("class", "d3-tip")
    .offset([40, -70])
    .html(function(d) {
      return (`${d.state}<br>Poverty: ${d.poverty}<br>Healthcare: ${d.healthcare}`);
    });
    svg.call(toolTip);

    //Create the overlay of the State Abbreviations
    chartGroup.append("g").selectAll("text")
        .data(Data)
        .enter()
        .append("text")
        .text(function (d) {
        return d.abbr;
        })
        .attr("dx", d => xLinearScale(d.poverty))
        .attr("dy", d => yLinearScale(d.healthcare)+5)
        .attr("class","stateText")
        .on('mouseover', toolTip.show)
        .on('mouseout', toolTip.hide);
    
    // Create Y Axis Label
    chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .classed("active",true)
    .text("Healthcare");

    // Create X Axis Label
  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .classed("active",true)
    .text("Poverty");
}