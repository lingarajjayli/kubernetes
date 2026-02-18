# Day 01: The Setup 🛠️

Today is all about getting your environment ready. We'll be using **Minikube** to run a local Kubernetes cluster and **k9s** to visualize it.

## 1. Start your Cluster
Run the following command to start Minikube using Docker as the driver:

```bash
minikube start --driver=docker
```

## 2. Install k9s
If you haven't already, install **k9s**. It's a terminal-based UI that makes interacting with Kubernetes a breeze.

- **On macOS (Homebrew):** `brew install derailed/k9s/k9s`
- **On Linux/Windows:** Follow the [official installation guide](https://k9scli.io/topics/install/).

## 3. Verify the Setup
Let's make sure everything is running smoothly. Check your nodes:

```bash
kubectl get nodes
```

You should see one node named `minikube` with a status of `Ready`.

## 4. Launch k9s
Just type `k9s` in your terminal. This is where you'll spend most of your time!

---
Next stop: [Day 02 - Your First Pod](../Day02/README.md)!
