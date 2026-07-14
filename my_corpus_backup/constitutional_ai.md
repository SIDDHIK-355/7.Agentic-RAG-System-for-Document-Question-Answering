[Skip to main content](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback#main-content)[Skip to footer](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback#footer)
[](https://www.anthropic.com/)
  * [Research](https://www.anthropic.com/research)
  * [Economic Futures](https://www.anthropic.com/economic-futures)
  * Commitments
  * Learn
  * [News](https://www.anthropic.com/news)


[Try Claude](https://claude.ai/)
AlignmentResearch
# Constitutional AI: Harmlessness from AI Feedback
15 Dec 2022
[Read Paper](https://arxiv.org/abs/2212.08073)
## Abstract
As AI systems become more capable, we would like to enlist their help to supervise other AIs. We experiment with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so we refer to the method as 'Constitutional AI'. The process involves both a supervised learning and a reinforcement learning phase. In the supervised phase we sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, we sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences. We then train with RL using the preference model as the reward signal, i.e. we use 'RL from AI Feedback' (RLAIF). As a result we are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.
## Policy Memo
[Constitutional AI Policy Memo](https://www-cdn.anthropic.com/7512771452629584566b6303311496c262da1006/Anthropic_ConstitutionalAI_v2.pdf)
[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)
## Related content
### Making Claude a chemist
[Read more](https://www.anthropic.com/research/making-claude-a-chemist)
### Coding agents in the social sciences
Results from a survey of 1,260 social scientists about AI and coding agent use.
[Read more](https://www.anthropic.com/research/coding-agents-social-sciences)
### Project Glasswing: An initial update
An early update on what we've learned from Project Glasswing. 
[Read more](https://www.anthropic.com/research/glasswing-initial-update)
[](https://www.anthropic.com/)
### Products
  * [Claude](https://claude.com/product/overview)
  * [Claude Code](https://claude.com/product/claude-code)
  * [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
  * [Claude Cowork](https://claude.com/product/cowork)
  * [Claude Security](https://claude.com/product/claude-security)
  * [Claude for Chrome](https://claude.com/chrome)
  * [Claude for Slack](https://claude.com/claude-for-slack)
  * [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
  * [Skills](https://www.claude.com/skills)
  * [Download app](https://claude.ai/download)
  * [Pricing](https://claude.com/pricing)
  * [Log in to Claude](https://claude.ai/)


### Models
  * [Mythos Preview](https://www.anthropic.com/glasswing)
  * [Opus](https://www.anthropic.com/claude/opus)
  * [Sonnet](https://www.anthropic.com/claude/sonnet)
  * [Haiku](https://www.anthropic.com/claude/haiku)


### Solutions
  * [AI agents](https://claude.com/solutions/agents)
  * [Code modernization](https://claude.com/solutions/code-modernization)
  * [Coding](https://claude.com/solutions/coding)
  * [Customer support](https://claude.com/solutions/customer-support)
  * [Education](https://claude.com/solutions/education)
  * [Enterprise](https://claude.com/solutions/enterprise)
  * [Financial services](https://claude.com/solutions/financial-services)
  * [Government](https://claude.com/solutions/government)
  * [Healthcare](https://claude.com/solutions/healthcare)
  * [Legal](https://claude.com/solutions/legal)
  * [Life sciences](https://claude.com/solutions/life-sciences)
  * [Nonprofits](https://claude.com/solutions/nonprofits)
  * [Security](https://claude.com/solutions/security)
  * [Small business](https://claude.com/solutions/small-business)
  * [Startups](https://claude.com/programs/startups)


### Claude Platform
  * [Overview](https://claude.com/platform/api)
  * [Developer docs](https://platform.claude.com/docs)
  * [Pricing](https://claude.com/pricing#api)
  * [Marketplace](https://claude.com/platform/marketplace)
  * [Regional compliance](https://claude.com/regional-compliance)
  * [Claude on AWS](https://claude.com/partners/claude-on-aws)
  * [Google Cloud’s Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)
  * [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
  * [Console login](https://platform.claude.com/)


### Resources
  * [Blog](https://claude.com/blog)
  * [Claude partner network](https://claude.com/partners)
  * [Community](https://claude.com/community)
  * [Connectors](https://claude.com/connectors)
  * [Courses](https://www.anthropic.com/learn)
  * [Customer stories](https://claude.com/customers)
  * [Engineering at Anthropic](https://www.anthropic.com/engineering)
  * [Events](https://www.anthropic.com/events)
  * [Inside Claude Code](https://www.anthropic.com/product/claude-code)
  * [Inside Claude Cowork](https://www.anthropic.com/product/claude-cowork)
  * [Inside Claude Enterprise](https://www.anthropic.com/product/enterprise)
  * [Inside Claude Security](https://www.anthropic.com/product/security)
  * [Plugins](https://claude.com/plugins)
  * [Powered by Claude](https://claude.com/partners/powered-by-claude)
  * [Service partners](https://claude.com/partners/services)
  * [Tutorials](https://claude.com/resources/tutorials)
  * [Use cases](https://claude.com/resources/use-cases)


### Help and security
  * [Availability](https://www.anthropic.com/supported-countries)
  * [Status](https://status.anthropic.com/)
  * [Support center](https://support.claude.com/en/)


### Company
  * [Anthropic](https://www.anthropic.com/company)
  * [Careers](https://www.anthropic.com/careers)
  * [Economic Futures](https://www.anthropic.com/economic-index)
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Claude’s Constitution](https://www.anthropic.com/constitution)
  * [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
  * [Security and compliance](https://trust.anthropic.com/)
  * [Transparency](https://www.anthropic.com/transparency)


### Terms and policies
  * [Privacy policy](https://www.anthropic.com/legal/privacy)
  * [Consumer health data privacy policy](https://www.anthropic.com/legal/consumer-health-data-privacy-policy)
  * [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
  * [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
  * [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
  * [Usage policy](https://www.anthropic.com/legal/aup)


© 2026 Anthropic PBC
  * [](https://www.linkedin.com/company/anthropicresearch)
  * [](https://x.com/AnthropicAI)
  * [](https://www.youtube.com/@anthropic-ai)


