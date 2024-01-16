
window.addEventListener('load', function () {
  console.log("DOM is loaded");

});
document.addEventListener("DOMContentLoaded", function () {
  // do things after the DOM loads partially
  console.log("DOM is loaded");
});

const delay = ms => new Promise(res => setTimeout(res, ms));
const yourFunction = async () => {
  await delay(3000);
  console.log("Waited for a few seconds");

  let adjacencyMatrix = data;
  let index = adjacencyMatrix.saving_index;
  let reverseindex = adjacencyMatrix.saving_reverseindex;

  var doctitle = document.title.split("-")[0].trim(); //Get document title
  console.log(doctitle);

  doctitle = document.title.split("-")[0].trim(); //Get document title
  try {
    let links_to_current_file = adjacencyMatrix[index[doctitle]];
    console.log(doctitle, index[doctitle],links_to_current_file);
    let links_to_current_file_names = links_to_current_file.map(x => `<a href="../${x}">${x}.md</a>`);
    console.log(links_to_current_file_names);
    // document.body.appendChild(document.createElement("div")).innerHTML = links_to_current_file_names.join("<br>");
    document.getElementsByClassName("container-fluid wm-page-content")[0].appendChild(document.createElement("div")).innerHTML = links_to_current_file_names.join("<br>");
    // document.getElementById("main-content").appendChild(document.createElement("div")).innerHTML = links_to_current_file_names.join("<br>");
  } catch (e) {
    doctitle = document.title.split("-")[0].trim(); //Get document title
    console.log(e);
  }
};

yourFunction();