(() => {
  function createSidebarToggle() {
    let isSidebarVisible = false;
    const toggleBtn = document.getElementById('toggleSidebar');
    const sidebarItems = document.getElementById('sidebarItems');
    const sidebar = document.getElementById('sidebar');

    function toggleSidebar() {
      if (isSidebarVisible) {
        sidebarItems.classList.add('sidebarItems-hidden');
        sidebarItems.classList.remove('sidebarItems-visible');

        sidebar.classList.add('sidebar-hidden');
        sidebar.classList.remove('sidebar-visible');
      } else {
        sidebarItems.classList.add('sidebarItems-visible');
        sidebarItems.classList.remove('sidebarItems-hidden');

        sidebar.classList.add('sidebar-visible');
        sidebar.classList.remove('sidebar-hidden');
      }
      isSidebarVisible = !isSidebarVisible;
    }

    toggleBtn.addEventListener('click', toggleSidebar);

    return { toggleSidebar };
  }

  createSidebarToggle();
})();
