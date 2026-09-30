# 📋 Process: Inbound Proposal & Contract Flow
1. **Lead Detection**: `crm.search` scans inbound requests and identifies client intent.
2. **Context Matching**: Agent loads `brain/company.md` and `brain/offer.md` to select scope.
3. **Proposal Drafting**: AGY drafts dual-language proposal specifications and milestone breakdown.
4. **Human Review Gate**: Triggers `approval.queued` notification for human sign-off.
5. **Dispatch & Notification**: Upon approval, generates client-facing PDF/DOCX and sends invite.
