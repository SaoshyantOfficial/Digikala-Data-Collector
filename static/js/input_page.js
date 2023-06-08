const addButton = document.getElementById('add-button');
    const deleteButton = document.getElementById('delete-button');
    const additionalFieldsContainer = document.getElementById('additional-fields-container');

    // Function to add a new URL text field
    const addUrlField = () => {
      // Find the number of existing URL text fields
      const numUrlInputs = document.querySelectorAll('input[name^="url"]').length;

      // Create a new URL text field with a unique ID and name
      const urlInput = document.createElement('input');
      urlInput.type = 'text';
      urlInput.name = `url${numUrlInputs + 1}`;
      urlInput.id = `url-input-${numUrlInputs + 1}`;
      urlInput.placeholder = `https://example.com`;
      urlInput.classList.add('form-control');

      // Create a new label for the URL text field
      const label = document.createElement('label');
      label.textContent = `Enter URL ${numUrlInputs + 1}:`;
      label.htmlFor = `url-input-${numUrlInputs + 1}`;
      label.classList.add('form-label');

      // Create a container for the label and URL input
      const additionalField = document.createElement('div');
      additionalField.classList.add('mb-3');
      additionalField.appendChild(label);
      additionalField.appendChild(urlInput);

      // Append the new URL text field to the container
      additionalFieldsContainer.appendChild(additionalField);
    };

    // Function to delete the last added URL text field
    const deleteUrlField = () => {
      // Find the last added URL text field
      const lastUrlInput = additionalFieldsContainer.lastChild;
      if (lastUrlInput !== null) {
        // Remove the last added URL text field
        additionalFieldsContainer.removeChild(lastUrlInput);
      }
    };

    addButton.addEventListener('click', addUrlField);
    deleteButton.addEventListener('click', deleteUrlField);



// check that all text fields should be fill
// Select the form and submit button
const form = document.querySelector('form');
const submitButton = document.querySelector('button[type="submit"]');

// Function to check if any URL field is empty
const checkEmptyFields = () => {
  const urlInputs = document.querySelectorAll('input[name^="url"]');
  let isEmpty = false;

  // Loop through each URL field and check if it's empty
  urlInputs.forEach((input) => {
    if (input.value.trim() === '') {
      isEmpty = true;
    }
  });

  return isEmpty;
};

// Add event listener to the submit button
submitButton.addEventListener('click', (event) => {
  // Call the checkEmptyFields function to see if any fields are empty
  if (checkEmptyFields()) {
    // Prevent the form from submitting
    event.preventDefault();

    // Alert the user to fill in the empty fields
    alert('Please fill in all URL fields.');
  }
});
