/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // './templates/**/*.html',
    // './templates/components/**/*.html',
    // './static/js/**/*.js',
    './**/templates/**/*.html.jinja2',
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
  safelist: [
    'sidebar-visible',
    'sidebar-hidden',
    'sidebar',
    'sidebarItems-visible',
    'sidebarItems-hidden',
    'sidebarItems',
  ]
}
