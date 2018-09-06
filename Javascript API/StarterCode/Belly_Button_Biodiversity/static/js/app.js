function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel
  var Metadata = `/metadata/${sample}`;
  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`
  d3.json(Metadata).then(function(response) {

  var panelData = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
  panelData.html("");

Object.entries(response).forEach(([key, value]) => {
    panelData.append("div").text(`${key}: ${value}`);
  });
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
  })
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var sampleData = `/samples/${sample}`;
  // @TODO: Build a Bubble Chart using the sample data
d3.json(sampleData).then(function(response) {
  var sample_values = response.sample_values;
  var otu_ids = response.otu_ids;
  var otu_labels = response.otu_labels;
  var trace1 = {
    x: otu_ids,
    y:sample_values,
    mode: 'markers',
    marker: {
      size: sample_values,
      color: otu_ids,
      colorscale: "Rainbow"
    },
    text: otu_labels
  };
  var data = [trace1];
  var layout = {
    height: 600,
    width: 1200,
  }
  Plotly.newPlot("bubble",data, layout);

});

  // @TODO: Build a Pie Chart
  d3.json(sampleData).then(function(response){
    var sample_values = response.sample_values.slice(0,10);
    var otu_ids = response.otu_ids.slice(0,10);
    var otu_labels = response.otu_labels.slice(0,10);
    var piedata = [{
      values: sample_values,
      labels: otu_ids,
      hovertext: otu_labels,
      type: 'pie'
    }];
    var layout = {
      height: 600,
      width: 600
    };
    Plotly.newPlot("pie",piedata,layout);

});



    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
