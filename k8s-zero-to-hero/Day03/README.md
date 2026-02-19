# Day 03: Doom & Self-Healing 🔫

Yesterday we ran a single Pod. But what happens if that Pod dies? In a real system, we want it to come back automatically. Today, we'll use a **Deployment** to manage multiple copies of **Doom**.

## 1. Deploy Doom
Apply the deployment configuration:

```bash
kubectl apply -f doom.yaml
```

## 2. See the Replicas
Open **k9s**. You should see **3** pods starting up. Kubernetes is making sure that 3 replicas of Doom are always running.

## 3. The Challenge: Kill a Pod! 💀
This is the "Self-Healing" magic of Kubernetes.

1. Open **k9s** and focus on one of the `doom` pods.
2. Press `Ctrl+D` (or the delete key) to kill that pod.
3. **Watch closely!** As soon as one pod dies, Kubernetes will immediately spin up a new one to maintain the 3-replica state you requested in `doom.yaml`.

## 4. Play Doom
Forward the port for any of the pods to play:

```bash
kubectl port-forward deployment/doom 8081:8080
```

Open your browser: [http://localhost:8081](http://localhost:8081)

## 💡 What happened?
A **Deployment** acts as a controller. You tell it the "Desired State" (3 replicas), and it works tirelessly to make sure the "Actual State" matches it. If a pod crashes or is deleted, the Deployment replaces it.

---
Great job! You've mastered the basics of self-healing. See you on Day 04!
