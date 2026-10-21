---
title: "8 eMudhra certificates are compromised. Here's what you need to know"
date: 2026-10-21 23:05:15 +0700
section: Research Summary
section_slug: research-summary
description: "Severity: Internet-wide server-impersonation risk."
audio: /audio/2026/10/8-emudhra-certificates-are-compromised-here-s-what-you-need-to-know.mp3
duration: "3 min 55 sec"
read_time: "3 min"
primary_source: https://blog.cloudflare.com/emudhra-certificate-compromise/
signal:
  - "Severity: Internet-wide server-impersonation risk."
  - "According to the supplied report, Cloudflare learned on October 19, 2026, at approximately 17:00 UTC that private keys…"
  - "Attackers could forge certificates for arbitrary domains to intercept or modify traffic."
---
## Cloudflare: eMudhra certificate-key compromise

**Severity:** Internet-wide server-impersonation risk. According to the supplied report, Cloudflare learned on **October 19, 2026, at approximately 17:00 UTC** that private keys for **eight widely trusted eMudhra intermediate certificates** were compromised. Attackers could forge certificates for arbitrary domains to intercept or modify traffic.

This concerns **certificate authentication—not TLS encryption algorithms**. Cloudflare’s review had found **no active exploitation on its services**.

### Cloudflare response
- Updated shared trust stores, base images, and services that authenticate remote endpoints, including origin connections and external API calls.
- Separately assessed applications with bundled or custom trust stores; activated changes through reloads, restarts, and image deployments.
- Published client and Tunnel fixes. CDN and server-side Zero Trust mitigations were fully deployed by **October 20, 19:20 UTC**; further remediation remained ongoing.
- The report says **Zero Trust with Gateway and an up-to-date client** is automatically protected.

### Fixed versions cited in the report

| Product | Versions |
|---|---|
| Cloudflare One Client | Android **v2.5.7**; iOS **v1.12.7** |
| 1.1.1.1 app | Android **v6.38.11**; iOS **v6.31.8** |
| Both clients: Windows, macOS, Linux | **2026.8.2115.0** |
| Cloudflare Tunnel (`cloudflared`) | **2026.10.2** |

### Remaining customer-controlled exposure
- **Mutual TLS:** customer-configured trust stores and uploaded CAs used to verify client certificates.
- **Origins:** custom origin certificates and server configurations under **Full (strict)** or **Strict** mode. Distrusted certificates can cause connection failures; Automatic SSL/TLS notifications were being updated.
- **Containers and Sandboxes:** certificate stores in container images and application dependencies. Containers with **HTTPS egress interception enabled** are already protected for intercepted connections because Cloudflare performs remote-server certificate validation.

### Implementation cautions
An SDK may delegate TLS verification to an HTTP library, language runtime, OS, or custom trust store. **Updating the SDK alone may not change certificate-validation policy.** Relevant dependencies can be indirect, and updated images or trust stores may require activation.

**Do not disable certificate verification to suppress resulting errors.** Browser or `curl` checks establish protection only for their own verification path—not necessarily a background application’s.

**Read-only next checks:** compare deployed versions with the table, inspect dependency trees and actual application trust-store ownership, and review origin/mTLS configurations and container egress settings. The supplied report does not identify the eight certificates individually, so it cannot establish certificate-specific exposure by itself.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [8 eMudhra certificates are compromised. Here's what you need to know](https://blog.cloudflare.com/emudhra-certificate-compromise/)
