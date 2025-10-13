
function highlight(text, terms) {
  const regex = new RegExp(`(${terms.join('|')})`, 'gi');
  return text.replace(regex, '<mark>$1</mark>');
}


document.addEventListener('DOMContentLoaded', () => {
  let searchIndex = [];


  fetch('/src/search/index.json')
    .then(res => res.json())
    .then(data => {
      searchIndex = data;
    });

  const input = document.getElementById('search-input');
  const resultsContainer = document.getElementById('search-results');

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();
    if (!query) {
      resultsContainer.innerHTML = '';
      return;
    }

    const terms = query.split(/\s+/);
    

    const results = searchIndex
      .map(item => {
        let score = 0;
        const inTitle = terms.some(term => item.title.toLowerCase().includes(term));
        const inDesc = terms.some(term => item.description.toLowerCase().includes(term));
        const inTags = terms.some(term => item.tags.join(' ').toLowerCase().includes(term));

        if (inTitle) score += 3;
        if (inDesc) score += 2;
        if (inTags) score += 1;

        return score > 0 ? { ...item, score } : null;
      })
      .filter(Boolean)
      .sort((a, b) => b.score - a.score);

    renderResults(results, terms);
  });

  function renderResults(results, terms) {
    resultsContainer.innerHTML = '';

    results.forEach(item => {
      const div = document.createElement('div');
      div.classList.add('search-result');

      div.innerHTML = `
        <a href="${item.url}">
          <strong>${highlight(item.title, terms)}</strong><br />
          <small>${highlight(item.description, terms)}</small>
        </a>
      `;

      resultsContainer.appendChild(div);
    });
  }
});
