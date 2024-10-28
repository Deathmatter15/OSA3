.PHONY: all clean run

# The name of the executable
EXECUTABLE = assignment3

# Path to the Python script
SCRIPT = Project/assignment3.py

# Default target
all: $(EXECUTABLE)

# Create the symbolic link to the Python script
$(EXECUTABLE):
	@echo "Creating symbolic link to $(SCRIPT)..."
	@ln -sf $(CURDIR)/$(SCRIPT) $(CURDIR)/$(EXECUTABLE)

# Clean target (optional)
clean:
	@echo "Cleaning up..."
	@rm -f $(EXECUTABLE)

# Run the Python script
run:
	@echo "Running the server..."
	@python3 $(SCRIPT) -l 12345 -p "happy"