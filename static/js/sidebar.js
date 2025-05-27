document.addEventListener("DOMContentLoaded", function() {
    const toggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    if (toggle && sidebar) {
        toggle.onclick = function() {
            sidebar.classList.toggle('open');
            if (sidebar.classList.contains('open')) {
                sidebar.style.marginLeft = '0';
            } else {
                sidebar.style.marginLeft = '-220px';
            }
        };
        // Default hidden (closed)
        sidebar.style.marginLeft = '-220px';
    }
});
