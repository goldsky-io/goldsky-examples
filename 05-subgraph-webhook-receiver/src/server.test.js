// Minimal smoke test, no test framework dependency.
// Starts the receiver, sends a signed and an unsigned payload, checks both.
process.env.GOLDSKY_WEBHOOK_SECRET = "whs_test_secret";
process.env.NODE_ENV = "test";

const { createApp } = await import("./server.js");

const app = createApp();
const server = app.listen(0);
const port = server.address().port;
const base = `http://127.0.0.1:${port}`;

async function post(secret) {
  const res = await fetch(`${base}/webhooks/goldsky`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...(secret ? { "goldsky-webhook-secret": secret } : {}),
    },
    body: JSON.stringify({
      entity: "Trade",
      op: "INSERT",
      data: { id: "0x1", price: "100" },
    }),
  });
  return res.status;
}

const okStatus = await post("whs_test_secret");
const badStatus = await post("wrong_secret");

server.close();

if (okStatus !== 200) {
  console.error(`FAIL: correct secret got status ${okStatus}, want 200`);
  process.exit(1);
}
if (badStatus !== 401) {
  console.error(`FAIL: wrong secret got status ${badStatus}, want 401`);
  process.exit(1);
}

console.log("OK: webhook receiver accepts correct secret, rejects wrong secret");
