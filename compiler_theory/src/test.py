# --- 1. Install Python Runtime ---
# Install the runtime version that matches the ANTLR tool version
!pip install antlr4-python3-runtime==4.13.1

# --- 2. Download ANTLR Tool (Java JAR) ---
# We'll download version 4.13.1, but any recent version should work
ANTLR_JAR = "antlr-4.13.1-complete.jar"
!wget https://www.antlr.org/download/{ANTLR_JAR}

# --- 3. Create a Bash Alias (for easy use of the ANTLR tool) ---
# We'll save the alias to a temporary file, then source it
ALIAS_COMMAND = f"alias antlr4='java -jar {ANTLR_JAR}'"
!echo "{ALIAS_COMMAND}" > ~/.bashrc
!source ~/.bashrc

print("Setup complete! ANTLR tool is ready to use.")