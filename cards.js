// Select all elements with the class 'panel'
const panels = document.querySelectorAll('.panel');

// Add a click event listener to each panel
panels.forEach(panel => {
    panel.addEventListener('click', () => {
        // When a panel is clicked, first remove the 'active' class from all panels
        removeActiveClasses();
        // Then, add the 'active' class to the one that was clicked
        panel.classList.add('active');
    });
});

// A helper function to remove the 'active' class from all panels
function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove('active');
    });
}
