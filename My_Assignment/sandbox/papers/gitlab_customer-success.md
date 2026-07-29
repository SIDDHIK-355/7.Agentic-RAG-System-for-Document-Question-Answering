The Customer Experience department is part of the GitLab Sales function who partners with our customers to deliver value and positive business outcomes throughout their journey with GitLab.

The team can be reached in Slack channel (internal only).

## Mission Statement

To deliver value to all customers by engaging in a consistent, repeatable, and scalable way across defined segments so that customers see the value in their investment with GitLab, and we retain and drive growth within our enterprise customers.

The mission of the Customer Experience Department is to provide these customers with experience in order to:

- Accelerate initial customer value
- Maximize long-term, sustainable customer value
- Improve overall customer satisfaction & referenceability
- Maximize the total value of the customer to GitLab

## North Star Metrics

Our top-level metrics are:

1. Renewal Rate of ATR (available to renew)
1. Growth ARR
1. Customer Outcomes Realized

### Customer Experience Teams

- Customer Success Manager handbook
- Customer Success Engineer handbook
- Customer Success Architect handbook
- Renewals Managers handbook

### Digital Strategy

- Digital Strategy handbook

### Demo Systems

- Demo Systems documentation

### Customer Success Decision Tree

CSMAE Decision Tree - internal only

## Account Team

The account team is comprised of the Strategic Account Executive/Account Executive, Solutions Architect (Enterprise), and Customer Success Manager.

More information about the account team

## Overlap Between Solution Architects and Customer Success Managers or Architects

SA owns 1) pre-sales technical evaluation and relationships prior to the initial sale and 2) tier upgrades and new business units (i.e., connected new) within an existing customer. CSM owns 1) post-sales customer relationship and 2) license upgrades within an existing customer.

More information on the transition and ownership between Pre-Sales and Post-Sales

## Other Resources

### Education and Enablement

As a Customer Experience team member, it is important to be continuously learning more about our product and related industry topics. The education and enablement handbook page provides a dashboard of aggregated resources that we encourage you to use to get up to speed.

### GitLab University

Visit the GitLab University handbook page for an overview of our public-facing learning platform.

## Customer Experience Playbooks

See the Playbooks Page

### Customer Workshops

CSM-Created, Enablement Focus:

- All CSM-created workshops

CSE-Created, Enablement Focus:

- GitLab User Webinars and Labs

### Using Salesforce within Customer Success

Visit this page for more info on using Salesforce within Customer Success.

### Using Gainsight with Customer Success

Visit this page for more information on using Gainsight within Customer Success.

### Using the Customer Feedback Form

Visit this page for more information on submitting Customer Feedback.

### Dogfooding

Outside of Engineering the Customer Experience team has the largest concentration of tooling development capability. The team has unique needs that can't always be solved by GitLab's single DevOps platform. However, it is important to dogfood and avoid dogfooding anti-patterns. As a result the Product organization heavily weights internal customers when considering prioritization. If you are considering building tooling in support of Customer Experience priorities outside of GitLab, please follow the dogfooding process.

### Customer Experience AWS Test Account

In an effort to keep AWS spend down, initiatives are being taken to automatically clean up our AWS account. This account is primarily used as a proof of concept for IaC and creating demos for GitLab customers. An automated cleanup script is currently being tested that will tag, shutdown and delete old resources as they are no longer needed. The automation will:

- Turn off and Tag Un-named resources. When resources are created a "Name" tag should be created with a value that's meaningful and indicates who deployed the resource. Example: {initials}-GitLabRunner
- New Resources will be automatically tagged with a Discovered and Expiration tag
- The Expiration tag is 14 days after the discovery. The script will only a tag an instance once. If you need additional time, please change the date to a reasonable date for cleanup (Add a month or two for prospective customers)
- If a resource needs to be permanent please set termination protection on the instance. This should also include tagging the instance with an explanation on why it's permanent and what its for
- On expiration the resource will be shut off and left for 7 days
- In 7 days if the instance is still off a snapshot will be taken and it will be terminated
- If the instance is still on but the expiration has not been changed it will be terminated

### Customer Experience Tools and Scripts

By customer or internal request, we sometimes develop tools to automate certain GitLab tasks using the API. The resulting tools and scripts are publicly available for everyone to use and contribute to in the GitLab CS Tools group.
**Note:** Those tools are not supported by GitLab Support.

### Communities of Practice

Community of Practice are cross-functional groups of SME's (or aspiring to be!) within the CX organization dedicated to a topic within GitLab or the broader DevOps space. The goal is to build assets, best practices, demonstrations, and share experiences we learn from prospects and customers. In turn, CoP will build broader technical depth within our CX organization to better advise our customers and influence our product roadmap.

## Customer Terrain Mapping Engagements

Terrain Mapping discovery engagements provide customers with the benefit of GitLab's experience with DevOps methodologies, Git, GitLab, CI, CD, and monitoring by brainstorming a high level, first draft discovery of the elements of a success plan to address various challenges. They are also mapped to professional services that can help with some of the elements identified in the engagement.

See the Terrain Mapping Engagements Page

### Frequently Asked Questions

Customer Experience team members maintain a FAQ to keep questions customers ask documented in a place where everyone can view and contribute to.

### Customer Experience resource links outside handbook

- Customer Reference Sheet
- Sales Collateral
- GitLab University
- Our Support Handbook
- Customer Collaboration Project template
- GitLab Demo Portal
- Workflow SA Demo Scenarios (Internal Only)
- SA-Created - Hands-On Workshops

### Other Sales Topics

- Sales Handbook
- Sales Operations
- Sales Skills Best Practices
- Sales Discovery Questions
- EE Product Qualification Questions
- GitLab Positioning
- FAQ from prospects
- Client Use Cases
- Proof of Value Guidelines
- Account Planning Template for Large/Strategic Accounts
- Sales Demo
- Sales Development Group Handbook
- With Whom to Talk to Ask Questions or Give Feedback on a GitLab feature

### Customer Experience Meetings

Customer Experience has a few standing meetings:

- CX Team Monthly All-Hands - Monthly on the second Wednesday
- Technical Skills Exchange (TSX) - Twice Monthly

The different groups within CX also have standing meetings, including meetings for the Customer Success teams and Renewal Managers, regional groups, and social calls.