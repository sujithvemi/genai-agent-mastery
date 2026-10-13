# R05 · SYSTEMS · SD-01 + SD-02 — the request path and the run API

**Lane:** SYSTEMS · **Repo:** project_management_building_agent (PM) · **Time:** 40 min · **Output:** sections §1 and §2 of `design/pm-agent-at-scale.md`

## Predict (5 min)
A user in team A clicks "plan this epic". Before opening anything, write the hops from the browser to the first model call **in production on GCP** (not today's laptop setup). Where is TLS terminated? Where is the user authenticated? Which component could reject the request for rate limit? What does the client get back immediately, given a run takes up to 2 minutes?
> _Predictions:_

## Read your code (10 min)
`src/pm_agent/api/app.py`: `POST /runs` (line ~192, returns **202**), `GET /runs/{id}`, `GET /runs/{id}/events`, `/cancel`, `/approve`, `/reject`, `/clarify`.
1. Why 202 and not 200 with the plan in the body?
2. What does `/events` give the client, and what transport would you pick for it in production (poll, SSE, WebSocket)? One line why.
3. What happens if the client retries `POST /runs` after a timeout? Is there an idempotency key? Compare with ARB `enforcement/idempotency.py`.
> _Answers:_

## Learn (15 min, pick ONE)
- Hello Interview — core concepts: API gateway + load balancer, *or*
- Backend from first principles — the HTTP / REST video, *or*
- Postman API Design — the async API / long-running operations video.
Note the 3 ideas you'll use.

## Apply (10 min)
Write §1 (request path: DNS → global HTTPS LB → API gateway or Cloud Run ingress → pm-agent API → worker → model/tool gateways; mark where TLS, auth, rate limiting and routing happen) and §2 (the run API: resources, 202 + events, idempotency key, error model, versioning) in `design/pm-agent-at-scale.md`. Add one row to its decisions log with the alternative you rejected.

## Done when
- [ ] §1 and §2 written by you
- [ ] You can answer "why is the run API asynchronous?" in two sentences
- [ ] LOG line + cards + ratings (`api/` row in the comprehension map)
