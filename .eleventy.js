module.exports = function(eleventyConfig) {
        // Aliases are in relation to the _includes folder
  eleventyConfig.addLayoutAlias('about', 'layouts/about.html');
  eleventyConfig.addLayoutAlias('book', 'layouts/book.html');
  eleventyConfig.addLayoutAlias('default', 'layouts/default.html');
        // Copy the `assets` directory to the compiled site folder
  eleventyConfig.addPassthroughCopy('assets');
  return {
    dir: {
      input: "./content/",      // Equivalent to Jekyll's source property
      output: "./_site" // Equivalent to Jekyll's destination property
    },
           passthroughFileCopy: true
  };
};
