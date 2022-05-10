const {
	readFileSync
} = require('fs');
const path = require('path');
const fs = require('fs');

const directoryPath = path.join(__dirname);
var re = /\[\[(.*?)\]\]/g;
const arrayColumn = (arr, n) => arr.map(x => x[n]);

fs.readdir(directoryPath, function (err, files) {
	//Build index first
	var allfiles = [];
	// Ignore if error
	if (err) {
		return console.log('Unable to scan directory: ' + err);
	}
	// Read all markdown files in directory and push cleaned up names to array
	files.forEach(function (file) {
		file = `docs/${file}`;
		if (file.includes("md") && !file.includes(".png")) {
			allfiles.push(file.replace("docs/", ""));
		};
	});

	// Build index and reverse index
	var indexdict = new Map();
	var reversedict = new Map();
	var counter = 0;
	allfiles.forEach(function (file) {
		indexdict.set(file.replace(".md", ""), counter);
		reversedict.set(counter, file.replace(".md", ""));
		counter++;
	});

	// Create adjacency matrix
	var adjacencyMatrix = new Map();
	var adjs = [];

	allfiles.forEach(function (file) {
		file = `docs/${file}`;
		//Read file
		var markdown = readFileSync(file, {
			encoding: 'utf8'
		});
		//Check if it has links
		var links = markdown.match(re);
		if (links != null) {
			//Clean up
			links = links.map(x => x.replace("]]", "").replace("[[", ""))
			links = links.map(x => indexdict.get(x)).filter(x => x);
			var newfilename = file.replace("docs/", "").replace(".md", "");
			//Replace with dictionary index
			var connections = indexdict.get(newfilename);
			//Create empty array with length of number of files
			(arr = []).length = allfiles.length;
			arr.fill(0);
			//Set connections to 1
			if (connections.length > 0) {
				connections.forEach(function (x) {
					x => arr[x] = 1
				});
			} else {
				arr[connections] = 1;
			}
			//Set adjacency matrix with connections
			// adjacencyMatrix.set(indexdict.get(newfilename), arr);
			adjs[indexdict.get(newfilename)] = arr;
		}

		// var arrayadjs = Array.from(adjacencyMatrix)
		// console.log(arrayadjs[44]);

		//Set adjacency matrix with custom parameters
		adjacencyMatrix.set("saving_index", Object.fromEntries(indexdict));
		adjacencyMatrix.set("saving_reverseindex", Object.fromEntries(reversedict));

	});

	indexdict.forEach(x => {
		// console.log(x);
		// maps = arrayColumn(adjs, x).findIndex(el => el == 1);
		var maps = arrayColumn(adjs, x);
		var mapindex = []
		maps.forEach(function (el, index) {
			if(el == 1){
				mapindex.push(index);
			};
		});
		// console.log(mapindex);
		if (!Array.isArray(mapindex)) {
			adjacencyMatrix.set(x, reversedict.get(mapindex));
		} else {
			mapindex = mapindex.map(y => reversedict.get(y));
			adjacencyMatrix.set(x, mapindex);
	}
	});


	// fs.writeFile('docs/searchindex.js', "let data=".concat(JSON.stringify(Object.fromEntries(adjacencyMatrix))), err => {
	// 	if (err) {
	// 		console.log(err);
	// 	}
	// });
});