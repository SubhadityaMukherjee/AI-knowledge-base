<!DOCTYPE html>
<html>
<head>
  <title>Random Points</title>
</head>
<body>
  <h1>Random Points</h1>
  <button onclick="showRandomPoints()">Show Random Points</button>
  <ul id="pointsList"></ul>

  <script>
    function showRandomPoints() {
      fetch('quotes.md')
        .then(response => response.text())
        .then(text => {
          const points = extractPoints(text);
          const randomPoints = getRandomPoints(points, 10);
          displayPoints(randomPoints);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }

    function extractPoints(text) {
      const lines = text.split('\n-');
      const points = lines.filter(line => line.trim());
      return points.map(point => point.trim());
    }

    function getRandomPoints(points, num) {
      const randomPoints = [];
      const availableIndices = Array.from(Array(points.length).keys());
      for (let i = 0; i < num; i++) {
        const randomIndex = Math.floor(Math.random() * availableIndices.length);
        const pointIndex = availableIndices.splice(randomIndex, 1)[0];
        randomPoints.push(points[pointIndex]);
      }
      return randomPoints;
    }

    function displayPoints(points) {
      const pointsList = document.getElementById('pointsList');
      pointsList.innerHTML = '';
      points.forEach(point => {
        const li = document.createElement('li');
        li.textContent = point;
        pointsList.appendChild(li);
      });
    }
  </script>
</body>
</html>

## Backlinks

> - [](index.md)
>   - Quotes collected from a lot of places over the years [[quotes]]

_Backlinks last generated 2023-05-28 11:11:44_
