// Receives subgraph-driven webhooks from Goldsky.
// Docs: https://docs.goldsky.com/subgraphs/guides/send-subgraph-driven-webhooks
import express from "express";

const WEBHOOK_SECRET = process.env.GOLDSKY_WEBHOOK_SECRET;

export function createApp() {
  const app = express();
  app.use(express.json());

  app.post("/webhooks/goldsky", (req, res) => {
    const secret = req.header("goldsky-webhook-secret");

    if (WEBHOOK_SECRET && secret !== WEBHOOK_SECRET) {
      return res.status(401).json({ error: "invalid webhook secret" });
    }

    const { entity, op, data } = req.body;
    console.log(`[goldsky webhook] entity=${entity} op=${op}`, data);

    res.status(200).json({ received: true });
  });

  return app;
}

if (process.env.NODE_ENV !== "test") {
  const port = process.env.PORT ?? 3000;
  createApp().listen(port, () => {
    console.log(`Webhook receiver listening on :${port}`);
  });
}
