const link = document.querySelector('a');
       
link.addEventListener('click', async (event) => {
  event.preventDefault();
  
  const response = await fetch(link.href);
  const data = await response.blob();
  
  const url = URL.createObjectURL(data);
  
  window.location.href = url;
});