document.addEventListener("DOMContentLoaded", function () {
  const next = document.querySelector(".next");
  const prev = document.querySelector(".prev");

  // When the DOM is ready, run the animations
  addActiveAnimation();

  // DOM reordering to cycle slides
  next.addEventListener('click', function(){
    let items = document.querySelectorAll('.slide .item');
    document.querySelector(".slide").appendChild(items[0]);
    setTimeout(addActiveAnimation, 50);
  });

  prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.slide .item');
    document.querySelector(".slide").prepend(items[items.length - 1]);
    setTimeout(addActiveAnimation, 50);
  });

  // Animation code for the active slide
  function addActiveAnimation() {
    const activeContent = document.querySelector(".slide .item:nth-child(1) .content");
    if (!activeContent) return;

    const elements = activeContent.querySelectorAll(".name, .welcome, .desc, button, .contact-item, .experience-sub-title, .section__text__p1, .skill-card");
    
    elements.forEach(el => {
      el.style.animation = "none";
      el.offsetHeight; // Trigger reflow
      el.style.animation = getAnimationForElement(el);
    });
  }

  function getAnimationForElement(el) {
    if (el.classList.contains("welcome")) return "animate 1s ease-in-out 0.3s forwards";
    if (el.classList.contains("contact-item")) {
      const index = Array.from(el.parentNode.children).indexOf(el);
      return `contactAppear 0.6s ease-out ${0.3 + index * 0.2}s forwards`;
    }
    if (el.classList.contains("skill-card")) {
      const index = Array.from(el.parentNode.children).indexOf(el);
      return `skillAppear 0.6s ease-out ${0.3 + index * 0.2}s forwards`;
    }
    if (el.classList.contains("experience-sub-title")) return "titleAppear 1s ease-out 0.3s forwards";
    if (el.classList.contains("section__text__p1")) return "titleAppear 1s ease-out 0.2s forwards";
    if (el.tagName === "BUTTON") return "button-animate 1s ease-in-out 0.3s forwards";
    return "animate 1s ease-in-out forwards";
  }

  // Project carousel functionality
  let currentProjectIndex = 0;
  const projectItems = document.querySelectorAll('.project-item');
  const projectDots = document.querySelectorAll('.project-dot');
  const projectNavBtns = document.querySelectorAll('.project-nav-btn');
  
  // Initialize the project carousel
  initProjectCarousel();
  
  function initProjectCarousel() {
    if (projectItems.length === 0) return;
    
    // Set first project as active
    showProject(0);
    
    // Update event listeners for the new navigation buttons
    const prevProjectBtns = document.querySelectorAll('.prev-project');
    const nextProjectBtns = document.querySelectorAll('.next-project');
    
    prevProjectBtns.forEach(btn => {
      btn.addEventListener('click', prevProject);
    });
    
    nextProjectBtns.forEach(btn => {
      btn.addEventListener('click', nextProject);
    });
    
    // Add click event listeners to dots
    projectDots.forEach((dot, index) => {
      dot.addEventListener('click', () => showProject(index));
    });

    // Also keep keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') prevProject();
      if (e.key === 'ArrowRight') nextProject();
    });
  }

  // Show specific project
  function showProject(index) {
    if (!projectItems.length) return;
    
    // Hide all projects
    projectItems.forEach(item => item.classList.remove('active'));
    projectDots.forEach(dot => dot.classList.remove('active'));
    
    // Calculate new index with wrapping
    currentProjectIndex = (index + projectItems.length) % projectItems.length;
    
    // Activate new project
    projectItems[currentProjectIndex].classList.add('active');
    if (projectDots.length > currentProjectIndex) {
      projectDots[currentProjectIndex].classList.add('active');
    }
  }

  // Next and previous project functions
  function nextProject() {
    showProject(currentProjectIndex + 1);
  }
  
  function prevProject() {
    showProject(currentProjectIndex - 1);
  }

  // Make functions accessible globally
  window.showProject = showProject;
  window.nextProject = nextProject;
  window.prevProject = prevProject;
  
  // Fix the contact slide navigation function to be more reliable
  window.goToContactSlide = function() {
    const items = document.querySelectorAll('.slide .item');
    
    // Better way to find the contact slide - more explicit check
    let contactIndex = -1;
    items.forEach((item, index) => {
      const nameElement = item.querySelector('.content .name');
      // Use a more precise check for the content text
      if (nameElement && nameElement.textContent.trim() === 'Contact') {
        contactIndex = index;
      }
    });

    console.log("Contact slide found at index:", contactIndex); // Debug output
    
    if (contactIndex > 0) {
      // Move slides until contact slide is at index 0
      for (let i = 0; i < contactIndex; i++) {
        const firstItem = document.querySelector('.slide').firstElementChild;
        document.querySelector('.slide').appendChild(firstItem);
      }
      setTimeout(addActiveAnimation, 50);
    } else {
      console.error("Contact slide not found"); // Debug output
    }
  };

  // Email copy to clipboard functionality
  window.copyEmailToClipboard = function(email, element) {
    navigator.clipboard.writeText(email).then(function() {
      // Success - show copied message
      const tooltip = element.querySelector('.copy-tooltip');
      tooltip.textContent = "Copied!";
      element.classList.add('copied');
      
      // Reset after 2 seconds
      setTimeout(() => {
        tooltip.textContent = "Click to copy";
        element.classList.remove('copied');
      }, 2000);
    }).catch(function() {
      // Error - fallback to older method if clipboard API fails
      const textArea = document.createElement("textarea");
      textArea.value = email;
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand("copy");
      document.body.removeChild(textArea);
      
      const tooltip = element.querySelector('.copy-tooltip');
      tooltip.textContent = "Copied!";
      element.classList.add('copied');
      
      setTimeout(() => {
        tooltip.textContent = "Click to copy";
        element.classList.remove('copied');
      }, 2000);
    });
  };

  // Play button for WhileVisualizer video demo
  document.querySelectorAll('.play-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      // Only trigger for WhileVisualizer (first project-item)
      const projectTitle = btn.closest('.project-title-container')?.querySelector('.project-title');
      if (projectTitle && projectTitle.textContent.trim() === "WhileVisualizer") {
        const modal = document.getElementById('whileVisualizerModal');
        const video = document.getElementById('whileVisualizerVideo');
        if (modal && video) {
          modal.style.display = 'flex';
          video.currentTime = 0;
          video.play();
        }
      }
    });
  });

  // Modal close logic
  const closeModalBtn = document.querySelector('.video-modal-close');
  if (closeModalBtn) {
    closeModalBtn.onclick = function() {
      const modal = document.getElementById('whileVisualizerModal');
      const video = document.getElementById('whileVisualizerVideo');
      if (modal && video) {
        modal.style.display = 'none';
        video.pause();
        video.currentTime = 0;
      }
    };
  }
  // Close modal when clicking outside the video
  const whileVisualizerModal = document.getElementById('whileVisualizerModal');
  if (whileVisualizerModal) {
    whileVisualizerModal.onclick = function(e) {
      if (e.target === this) {
        this.style.display = 'none';
        const video = document.getElementById('whileVisualizerVideo');
        if (video) {
          video.pause();
          video.currentTime = 0;
        }
      }
    };
  }

  // Play button for Dapr Dash GIF demo
  document.querySelectorAll('.play-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const projectTitle = btn.closest('.project-title-container')?.querySelector('.project-title');
      if (projectTitle && projectTitle.textContent.trim() === "Dapr Dash") {
        const modal = document.getElementById('daprDashModal');
        if (modal) {
          modal.style.display = 'flex';
        }
      }
    });
  });

  // Modal close logic for Dapr Dash GIF
  const closeGifModalBtn = document.querySelector('.gif-modal-close');
  if (closeGifModalBtn) {
    closeGifModalBtn.onclick = function() {
      const modal = document.getElementById('daprDashModal');
      if (modal) {
        modal.style.display = 'none';
      }
    };
  }
  // Close GIF modal when clicking outside the image
  const daprDashModal = document.getElementById('daprDashModal');
  if (daprDashModal) {
    daprDashModal.onclick = function(e) {
      if (e.target === this) {
        this.style.display = 'none';
      }
    };
  }
});
