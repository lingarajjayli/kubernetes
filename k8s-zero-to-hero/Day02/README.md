# Day 02: Your First Pod (2048 Game) 🧩

Today, we're deploying a classic: the 2048 game. This will be your first **Pod**—the smallest deployable unit in Kubernetes.

## 1. Deploy the Game
Use `kubectl` to apply the YAML configuration:

```bash
kubectl apply -f 2048-pod.yaml
```

## 2. Check the Status
Wait for the pod to be `Running`. You can check this in **k9s** or by running:

```bash
kubectl get pods
```

## 3. Play the Game!
Since the pod is running inside the cluster, we need to "forward" the port to our local machine to access it:

```bash
kubectl port-forward pod/game-2048 8080:80
```

Now, open your browser and go to:
👉 [http://localhost:8080](http://localhost:8080)

## 💡 What happened?
You just told Kubernetes to pull a Docker image (`alexwhen/docker-2048`) and run it as a Pod. Kubernetes is now managing that container for you!

---
Next stop: [Day 03 - Doom & Self-Healing](../Day03/README.md)!
