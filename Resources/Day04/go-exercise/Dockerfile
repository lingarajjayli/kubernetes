# STAGE 1: The Builder
# We use the full Go image to compile our code
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Copy the source code
COPY main.go .

# Compile the application into a single binary named 'hello'
RUN go build -o hello main.go

# ---------------------------------------------------------

# STAGE 2: The Final Product
# We switch to a tiny Linux distribution (Alpine)
FROM alpine:latest

WORKDIR /root/

# MAGIC LINE: Copy only the compiled binary from the 'builder' stage
COPY --from=builder /app/hello .

# Run the binary
CMD ["./hello"]
# ---------------------------------------------------------