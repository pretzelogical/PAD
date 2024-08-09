(() => {
/**
 * Creates a toggle button for the sidebar. When clicked, it toggles the
 * visibility of the sidebar.
 *
 * @return {Object} An object with a `toggleSidebar` method that can be used to
 * toggle the sidebar visibility.
 */
  function createSidebar() {
    let isSidebarVisible = false;
    const toggleBtn = document.getElementById('toggleSidebar');
    const sidebarItems = document.getElementById('sidebarItems');
    const sidebar = document.getElementById('sidebar');
    const disclaimerBtn = document.getElementById('showDisclaimer');
    const disclaimerPopup = document.getElementById('disclaimerPopup');
    const closeDisclaimerBtn = document.getElementById('closeDisclaimer');

    /**
     * Toggles the visibility of the sidebar.
     *
     * @return {undefined}
     */
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

    function showDisclaimer() {
      disclaimerPopup.classList.remove('hidden');
    }

    function closeDisclaimer() {
      disclaimerPopup.classList.add('hidden');
    }

    toggleBtn.addEventListener('click', toggleSidebar);
    disclaimerBtn.addEventListener('click', showDisclaimer);
    closeDisclaimerBtn.addEventListener('click', closeDisclaimer);
    disclaimerPopup.addEventListener('click', (e) => {
      if (e.target === disclaimerPopup) closeDisclaimer();
    });

    return { toggleSidebar, showDisclaimer, closeDisclaimer };
  }

  createSidebar();
})();
