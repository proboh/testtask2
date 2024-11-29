# testtask2

Task 2: Signal Bot with ATAK Integration
  Objective: Create a Signal bot to send geolocation and target information to an ATAK (Android Team Awareness Kit) client.
Steps:
 1. Design a Python-based Signal bot that can send messages like:
   "48.567123 39.87897 tank" (longitude, latitude, target description).
 2. Format the message in Cursor on Target (CoT) protocol.
 3. Send the formatted CoT message to an ATAK client (https://www.civtak.org/).
 4. Ensure that the message is displayed in the ATAK client interface.
Breakdown of Steps:
 1. Install Signal-CLI
  You will first need to install Signal-CLI on your system. If you haven't already, follow these steps:
  Download Signal-CLI from the Signal-CLI GitHub page.
  Extract it and install any necessary dependencies (Java, etc.).
 2. Set up an account
  For linking with an existing (master) device:
    ./signal-cli link -n "optional device name"
  This shows a sgnl://linkdevice… link. If you want to link to an mobile device, create a QR code with the link and scan that in the Signal app.
  For registering a new master device:
    ./signal-cli -u +4915151111111 register
  After a few seconds, you will receive an SMS on the cell phone with phone number +4915151111111 that contains the verification code (123-456 in this example). Verify your phone number Enter:
    ./signal-cli -u +4915151111111 verify 123-456
 3. Send a first message from the command line
    ./signal-cli -u +4915151111111 send -m "My first message from the CLI" +4915152222222
 4. WIP
