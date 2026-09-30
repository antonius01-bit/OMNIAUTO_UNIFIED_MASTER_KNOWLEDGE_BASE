# 💳 Process: Milestone Invoicing & Payment Reconciliation
1. **Milestone Completion**: Code merged to main or research draft reviewed with 0 errors.
2. **Invoice Generation**: Pull billing rates and generate invoice record with cryptographic transaction reference.
3. **Ledger Update**: Append record to `sheets.append` and local ledger.
4. **Reconciliation**: Match incoming bank/crypto payment and mark milestone closed in CRM.
