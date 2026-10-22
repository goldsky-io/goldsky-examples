// Call Ethereum mainnet through Goldsky Edge RPC with viem.
// Uses the shared public "demo" key: rate limited, fine for this example.
// Replace "demo" with your own key from https://app.goldsky.com for real use.
import { createPublicClient, http } from "viem";
import { mainnet } from "viem/chains";

const key = process.env.GOLDSKY_API_KEY ?? "demo";

const client = createPublicClient({
  chain: mainnet,
  transport: http(`https://edge.goldsky.com/standard/evm/1?key=${key}`),
});

const blockNumber = await client.getBlockNumber();
console.log("Block number:", blockNumber.toString());
