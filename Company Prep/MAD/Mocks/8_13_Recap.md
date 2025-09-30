# Reviewing Sys Design Diagram Drawn for Oath

## Opportunities for Improvement

1. Scaling, Fault Tolerance
    - Discussion and consideration for scaling
        * How services, dbs scale horizontally (sharding/replication)
        * Rate limiting, retry logic, circuity breakers if Stripe is unavailable
    - Consider what occurs in case of service/vendor downtime
        * Solution: Queues, Async Processing, Eventual Consistency

2. Event-Driven/Async Flows
    - Use of message queues for donation processing, handling of donation processing retries, audit logs, notification sending (donation has occurred)
    - If during peak events, donations are delayed -> describe how requests are to be buffered + processed reliably w/o loss

3. User Experience and Feedback
- Map out confirmation flows -> donation success/failure notifications, email receipts, real time activity dashboards
- Approach for updating campaign progress following donations

4. Response Handling
- Expand on error response bodies, idempotency for repeated donation calls

5. Testing and CI/CD

6. Security, Data Privacy
    - Secure sensitive data -> payment info tokenization, PCI compliance
    - Audit logging, storage encryption

7. Monitoring, Observability
- Real time monitoring, error tracking, dashboards for admins

## For next Interview
* Start with req clarification then iterate on feedback
* Maintain awareness of consistency, availability trade-offs
* Structure discussion around scaling, third party outages, real-world user scenarios

## Personal Complaints
- Hadn't clarified API endpoints well
- Hadn't included Campaigns service as being distinct/separate from ledger (donations db)
