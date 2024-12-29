function openModal(content, type, caption = '') {
  const modal = document.getElementById('imageModal');
  const modalContent = document.getElementById('modalContent');
  const modalCaption = document.getElementById('modalCaption');
  modal.style.display = 'block';
  
  modalContent.innerHTML = `<img src="${content}" alt="Full size image">`;
  
  modalCaption.textContent = caption;
}

function closeModal() {
  document.getElementById('imageModal').style.display = 'none';
}

document.getElementById('imageModal')?.addEventListener('click', function(e) {
  if (e.target === this) {
    closeModal();
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeModal();
  }
});

const lastEditDate = '2024-12-29';
document.getElementById('lastUpdated').textContent = new Date(lastEditDate).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });