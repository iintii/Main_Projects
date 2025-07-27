document.addEventListener("DOMContentLoaded", function () {
  const next = document.querySelector(".next");
  const prev = document.querySelector(".prev");

  // When the DOM is ready, run the animations
  addActiveAnimation();

  // DOM reordering to cycle slides
  next.addEventListener('click', function () {
    let items = document.querySelectorAll('.slide .item');
    document.querySelector(".slide").appendChild(items[0]);
    setTimeout(addActiveAnimation, 50);
  });

  prev.addEventListener('click', function () {
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
    if (el.tagName === "BUTTON") return "animate 1s ease-in-out 0.3s forwards";
    return "animate 1s ease-in-out forwards";
  }

  // Project carousel functionality
  let currentProjectIndex = 0;
  const projectItems = document.querySelectorAll('.project-item');
  const projectDots = document.querySelectorAll('.project-dot');

  function initProjectCarousel() {
    if (projectItems.length === 0) return;

    showProject(0);

    // Navigation buttons
    document.querySelectorAll('.prev-project').forEach(btn => {
      btn.addEventListener('click', prevProject);
    });

    document.querySelectorAll('.next-project').forEach(btn => {
      btn.addEventListener('click', nextProject);
    });

    // Dots navigation
    projectDots.forEach((dot, index) => {
      dot.addEventListener('click', () => showProject(index));
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') prevProject();
      if (e.key === 'ArrowRight') nextProject();
    });
  }

  initProjectCarousel();

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
  window.goToContactSlide = function () {
    const items = document.querySelectorAll('.slide .item');
    let contactIndex = -1;

    items.forEach((item, index) => {
      const nameElement = item.querySelector('.content .name');
      if (nameElement && nameElement.textContent.trim() === 'Contact') {
        contactIndex = index;
      }
    });

    if (contactIndex > 0) {
      for (let i = 0; i < contactIndex; i++) {
        const firstItem = document.querySelector('.slide').firstElementChild;
        document.querySelector('.slide').appendChild(firstItem);
      }
      setTimeout(addActiveAnimation, 50);
    }
  };

  // Email copy to clipboard functionality
  window.copyEmailToClipboard = function (email, element) {
    const tooltip = element.querySelector('.copy-tooltip');
    const showCopied = () => {
      tooltip.textContent = "Copied!";
      element.classList.add('copied');
      setTimeout(() => {
        tooltip.textContent = "Click to copy";
        element.classList.remove('copied');
      }, 2000);
    };

    navigator.clipboard.writeText(email).then(showCopied).catch(() => {
      // Fallback for older browsers
      const textArea = document.createElement("textarea");
      textArea.value = email;
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand("copy");
      document.body.removeChild(textArea);
      showCopied();
    });
  };

  // Consolidated modal functionality
  function setupModals() {
    const videoModal = document.getElementById('whileVisualizerModal');
    const gifModal = document.getElementById('daprDashModal');
    const video = document.getElementById('whileVisualizerVideo');

    // Close buttons
    document.querySelector('.video-modal-close')?.addEventListener('click', () => {
      videoModal.style.display = 'none';
      video?.pause();
      if (video) video.currentTime = 0;
    });

    document.querySelector('.gif-modal-close')?.addEventListener('click', () => {
      gifModal.style.display = 'none';
    });

    // Click outside to close
    videoModal?.addEventListener('click', (e) => {
      if (e.target === videoModal) {
        videoModal.style.display = 'none';
        video?.pause();
        if (video) video.currentTime = 0;
      }
    });

    gifModal?.addEventListener('click', (e) => {
      if (e.target === gifModal) {
        gifModal.style.display = 'none';
      }
    });
  }

  // Play button functionality
  document.querySelectorAll('.play-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      const projectTitle = btn.closest('.project-title-container')?.querySelector('.project-title');
      const titleText = projectTitle?.textContent.trim();

      if (titleText === "WhileVisualizer") {
        const modal = document.getElementById('whileVisualizerModal');
        const video = document.getElementById('whileVisualizerVideo');
        if (modal && video) {
          modal.style.display = 'flex';
          video.currentTime = 0;
          video.play();
        }
      } else if (titleText === "Dapr Dash") {
        const modal = document.getElementById('daprDashModal');
        if (modal) {
          modal.style.display = 'flex';
        }
      }
    });
  });

  setupModals();
});
