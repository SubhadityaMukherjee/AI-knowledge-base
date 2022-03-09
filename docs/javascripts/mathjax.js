window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
		chtml: {
				scale: 1.3
		},
		svg:{
				scale: 1.3
		}
};

document$.subscribe(() => {
  MathJax.typesetPromise()
})

