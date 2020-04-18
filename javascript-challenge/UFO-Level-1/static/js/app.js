// from data.js
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

// Append the full data to the table
tableData.forEach((report) => {
    var row = tbody.append("tr");
    Object.entries(report).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
    });
});

// Get a reference to the button on the page 
var selectButton = d3.select("#filter-btn");

// Create a custom filtering function throughout the table
function filter() {
    // Declare variables
    var inputValue = d3.select("#datetime").node().value;
    table = document.getElementById("ufo-table");
    tr = table.getElementsByTagName("tr");
     // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(inputValue) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
        
// Use the `on` function in d3 to attach an event to the filter function
selectButton.on("click", filter);
