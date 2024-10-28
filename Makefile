.PHONY: all clean run

# Executable name.
EXECUTABLE = assignment3

# Path to the Python script.
SCRIPT = Project/assignment3.py

#Default Target
all: set_permissions $(EXECUTABLE)

#Ensure Python script permissions.
set_permissions:
	@echo "Setting executable permissions for $(SCRIPT)"
	chmod +x $(SCRIPT)


# Symbolic link to the Python script.
$(EXECUTABLE):
	@echo "Creating symbolic link to $(SCRIPT)"
	@ln -sf $(CURDIR)/$(SCRIPT) $(CURDIR)/$(EXECUTABLE)

# Clean target.
clean:
	@echo "Cleaning up..."
	@rm -f $(EXECUTABLE)

# Default run arguments.
run:
	@echo "Running the server..."
	@python3 $(SCRIPT) -l 12345 -p "happy"