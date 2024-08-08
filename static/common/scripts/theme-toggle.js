// theme-toggle.js
const themeToggleBtn = document.getElementById('theme-toggle');
const darkIcon = document.getElementById('theme-toggle-dark-icon');
const lightIcon = document.getElementById('theme-toggle-light-icon');

// Check for saved user preference, if any, on load of the website
if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark');
  darkIcon.classList.remove('hidden');
} else {
  document.documentElement.classList.remove('dark');
  lightIcon.classList.remove('hidden');
}

themeToggleBtn.addEventListener('click', () => {
  // Toggle icons inside button
  darkIcon.classList.toggle('hidden');
  lightIcon.classList.toggle('hidden');

  // If set via local storage previously
  if (localStorage.getItem('theme')) {
    if (localStorage.getItem('theme') === 'light') {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }

  // If NOT set via local storage previously
  } else {
    if (document.documentElement.classList.contains('dark')) {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      document.documentElement.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
  }
});
