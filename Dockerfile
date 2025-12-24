FROM python:3.12-slim

WORKDIR /app

# Install hatchling first
RUN pip install --no-cache-dir hatchling

# Copy package files
COPY pyproject.toml README.md LICENSE ./
COPY src/ ./src/

# Install the package
RUN pip install --no-cache-dir .

# Set the entry point
CMD ["python"]
