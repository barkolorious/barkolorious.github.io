// Project data stored directly in the JavaScript file to avoid CORS issues
const projectsData = {
  "projects": [
    {
      "id": "borealis",
      "title": "borealis Logo",
      "tags": ["Logo"],
      "description": "Logo for borealis"
    },
    {
      "id": "das_coffeetal",
      "title": "Das Coffeetal",
      "tags": ["Logo"],
      "description": "Logo for an imaginary concept coffee shop \"Das Coffeetal\"."
    },
    {
      "id": "believers_never_die",
      "title": "Be(lie)vers Never Die",
      "tags": ["Playlist Cover"],
      "description": "Playlist cover for borealis"
    },
    {
      "id": "barkolorious",
      "title": "barkolorious Logo",
      "tags": ["Logo"],
      "description": "My logo which represents a blackhole"
    },
    {
      "id": "opaque",
      "title": "opaque Logo",
      "tags": ["Logo"],
      "description": "Logo design for my project \"opaque: Open-source Portable Air Quality Evaluator\""
    },
    {
      "id": "aerop",
      "title": "AEROP Logo",
      "tags": ["Logo"],
      "description": "Logo for yavuzskarahan's project \"AEROP\"."
    },
    {
      "id": "fource",
      "title": "Fource Logo",
      "tags": ["Logo"],
      "description": "Logo design for my project \"Fource: Fourier based Complex Encryption\""
    },
    {
      "id": "liselerde_bilim_uygulamalari",
      "title": "LBU Logo Redisgn",
      "tags": ["Logo", "Redesign"],
      "description": "Redesigning the LBU logo."
    },
    {
      "id": "airqm",
      "title": "AirQ-M",
      "tags": ["Logo"],
      "description": "Logo for my project \"AirQ-M: Air Quality Meter\""
    }
  ]
};

// Function to create a portfolio item element
function createPortfolioItem(project) {
  const portfolioItem = document.createElement('a');
  portfolioItem.href = `projects/${project.id}.html`;
  portfolioItem.className = 'portfolio-item';

  portfolioItem.innerHTML = `
    <div class="image-container">
      <img src="assets/${project.id}/img00.png" alt="${project.title}">
    </div>
    <div class="item-content">
      <h2>${project.title}</h2>
      <div class="tags">
        ${project.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
      </div>
      <p>${project.description}</p>
    </div>
  `;

  return portfolioItem;
}

// Function to load and render projects
function loadProjects() {
  try {
    const portfolioGrid = document.querySelector('.portfolio-grid');
    
    // Clear existing content
    portfolioGrid.innerHTML = '';
    
    // Add each project to the grid
    projectsData.projects.forEach(project => {
      const portfolioItem = createPortfolioItem(project);
      portfolioGrid.appendChild(portfolioItem);
    });

  } catch (error) {
    console.error('Error loading projects:', error);
    // Show error message to user
    const portfolioGrid = document.querySelector('.portfolio-grid');
    portfolioGrid.innerHTML = '<p class="error">Failed to load projects. Please try again later.</p>';
  }
}

// Load projects when the DOM is ready
document.addEventListener('DOMContentLoaded', loadProjects);

// Error handling for images
document.addEventListener('error', function(e) {
  if (e.target.tagName.toLowerCase() === 'img') {
    e.target.src = 'assets/placeholder.png'; // Replace with your placeholder image
  }
}, true);