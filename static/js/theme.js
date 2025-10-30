function toggleTheme() {
	const html = document.documentElement;
	// Toggle the 'dark' class on the <html> element
	html.classList.toggle('dark');
	
	// Save the theme preference in localStorage
	if (html.classList.contains('dark')) {
		localStorage.setItem('theme', 'dark');
	} else {
		localStorage.setItem('theme', 'light');
	}
}

// On page load, set the theme based on localStorage
window.onload = function() {
	const savedTheme = localStorage.getItem('theme');
	if (savedTheme) {
		if (savedTheme === 'dark') {
			document.documentElement.classList.add('dark');
		} else {
			document.documentElement.classList.remove('dark');
		}
	} else {
		// Default to light theme if no theme is saved
		document.documentElement.classList.remove('dark');
	}
};