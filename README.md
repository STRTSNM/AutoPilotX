# AutopilotX

This project provides a user-friendly, drag-and-drop interface to define and execute automation tasks. Users can craft automation flows and save and load them for future execution.

## Features

* **Intuitive Drag-and-Drop Interface:** Easily build automation sequences by dragging and dropping actions onto the workspace.
* **Customizable Actions:** Configure different actions:
    * **Command:** Execute system commands (e.g., RunCommand)
    * **Mouse:** Simulate mouse actions (e.g., ClickElement)
    * **Keyboard:** Automate keyboard input (e.g., Hello, World!)
    * **Wait:** Introduce delays into your automation flow
* **Save and Load Flows:** Store your automation creations and reload them for later execution.
* **Execution Trigger:** A "Run" button to initiate the execution of the defined automation flow.

## Getting Started

1. Clone the repository.
2. Install dependencies (Eel for web-Python interaction).
3. Run `index.html` in your web browser.

## Usage

1. **Drag and Drop:** Pull actions from the buttons side to the blocks side.
2. **Configure:** When dropping an action, a modal allows for additional input customization.
3. **Save (optional):** Save your automation flow for later use.
4. **Run:** Click the "Run" button to execute your automation.

## Contributing

We welcome contributions to the project! Feel free to open issues for bug reports and feature requests or create pull requests to directly propose changes.

## Roadmap

* **More Action Types:** Expand the capabilities with actions like:
    * File manipulation (open, copy, delete)
    * Website interactions (fill forms, navigate)
    * Network requests (send/receive data)
* **Conditional Logic:** Enable if/else statements for more complex flow control.
* **Scheduling:** Allow users to execute automation flows at specific times or intervals.
* **Cloud Integration:** Provide options to save and load flows from cloud storage (e.g., Google Drive, Dropbox).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
