/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // './templates/**/*.html',
    // './templates/components/**/*.html',
    // './static/js/**/*.js',
    './**/templates/**/*.html.jinja2',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
