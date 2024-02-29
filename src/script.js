const blocksList = [];

document.addEventListener("DOMContentLoaded", function() {
  const buttons = document.querySelectorAll(".button-side button");

  buttons.forEach(button => {
    button.addEventListener("dragstart", function(e) {
      e.dataTransfer.setData("text/plain", button.id);
    });
  });
});

function allowDrop(event) {
  event.preventDefault();
}

function drop(event) {
  event.preventDefault();
  const buttonId = event.dataTransfer.getData('text/plain');
  const button = document.getElementById(buttonId);

  if (button) {
    const blockSide = document.getElementById('blockSide');

    // Prompt user for additional information based on the button type
    const modal = document.getElementById('modal');
    const modalLabel = document.getElementById('modalLabel');
    const modalInput = document.getElementById('modalInput');
    const modalSubmit = document.getElementById('modalSubmit');

    modal.style.display = 'block';

    // Set different hints based on the button type
    if (button.id === 'commandButton') {
      modalLabel.textContent = 'Enter the command:';
      modalInput.placeholder = '';
      modalInput.value = 'RunCommand'; // Default value for command
    } else if (button.id === 'mouseButton') {
      modalLabel.textContent = 'Enter the mouse action:';
      modalInput.placeholder = '';
      modalInput.value = 'ClickElement'; // Default value for mouse action
    } else if (button.id === 'keyboardButton') {
      modalLabel.textContent = 'Enter the text to input to keyboard:';
      modalInput.placeholder = '';
      modalInput.value = 'Hello, World!'; // Default value for keyboard input
    }

    modalSubmit.onclick = function () {
      const userInput = modalInput.value.trim();
      if (userInput !== '') {
        const blockValue = createBlock(blockSide, button, userInput);
        blocksList.push({ type: button.id, value: blockValue });
        modal.style.display = 'none';

        // Call the newly created exposed function with the added block details
        onBlockAdded(blockValue, button.id); // Replace 'onBlockAdded' with your actual function name
      }
    };

    // Close the modal when the '×' is clicked
    const closeBtn = document.querySelector('.close');
    closeBtn.onclick = function () {
      modal.style.display = 'none';
    };

    // Close the modal if the user clicks outside of it
    window.onclick = function (event) {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    };
  }
}

function createBlock(parent, button, content) {
  const block = button.cloneNode(true);
  let blockClass = '';

  if (button.id === 'commandButton') {
    blockClass = 'block command-block';
  } else if (button.id === 'mouseButton') {
    blockClass = 'block mouse-block';
  } else if (button.id === 'keyboardButton') {
    blockClass = 'block keyboard-block';
  } else if (button.id === 'waitButton') {
    blockClass = 'block wait-block'; // New class for wait button
  }

  block.setAttribute('class', blockClass);
  block.innerText = content;
  parent.appendChild(block);

  return content;
}

eel.expose(onBlockAdded);
// New function exposed to the outside world (replace 'onBlockAdded' with your actual function name)
function onBlockAdded(blockValue, blockType) {
  eel.appendlist(blockType,blockValue)
  console.log("New block added:", blockValue, blockType); // Example usage
}

document.getElementById("runButton").addEventListener("click", function() {
    eel.execution();
});


