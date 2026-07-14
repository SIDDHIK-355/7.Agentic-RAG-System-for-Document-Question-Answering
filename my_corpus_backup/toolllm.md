[Skip to main content](https://arxiv.org/abs/2307.16789#content)
[![Cornell University](https://arxiv.org/static/browse/0.3.4/images/icons/cu/cornell-reduced-white-SMALL.svg)](https://www.cornell.edu/)
[Learn about arXiv becoming an independent nonprofit.](https://tech.cornell.edu/arxiv/)
We gratefully acknowledge support from the Simons Foundation, [member institutions](https://info.arxiv.org/about/ourmembers.html), and all contributors. [Donate](https://info.arxiv.org/about/donate.html)
[](https://arxiv.org/IgnoreMe)
[![arxiv logo](https://arxiv.org/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)](https://arxiv.org/) > [cs](https://arxiv.org/list/cs/recent) > arXiv:2307.16789 
[Help](https://info.arxiv.org/help) | [Advanced Search](https://arxiv.org/search/advanced)
All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text
Search
[![arXiv logo](https://arxiv.org/static/browse/0.3.4/images/arxiv-logomark-small-white.svg)](https://arxiv.org/)
[ ![Cornell University Logo](https://arxiv.org/static/browse/0.3.4/images/icons/cu/cornell-reduced-white-SMALL.svg) ](https://www.cornell.edu/)
GO
## quick links
  * [Login](https://arxiv.org/login)
  * [Help Pages](https://info.arxiv.org/help)
  * [About](https://info.arxiv.org/about)


# Computer Science > Artificial Intelligence
**arXiv:2307.16789** (cs) 
[Submitted on 31 Jul 2023 ([v1](https://arxiv.org/abs/2307.16789v1)), last revised 3 Oct 2023 (this version, v2)]
#  Title:ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs
Authors:[Yujia Qin](https://arxiv.org/search/cs?searchtype=author&query=Qin,+Y), [Shihao Liang](https://arxiv.org/search/cs?searchtype=author&query=Liang,+S), [Yining Ye](https://arxiv.org/search/cs?searchtype=author&query=Ye,+Y), [Kunlun Zhu](https://arxiv.org/search/cs?searchtype=author&query=Zhu,+K), [Lan Yan](https://arxiv.org/search/cs?searchtype=author&query=Yan,+L), [Yaxi Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+Y), [Yankai Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+Y), [Xin Cong](https://arxiv.org/search/cs?searchtype=author&query=Cong,+X), [Xiangru Tang](https://arxiv.org/search/cs?searchtype=author&query=Tang,+X), [Bill Qian](https://arxiv.org/search/cs?searchtype=author&query=Qian,+B), [Sihan Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+S), [Lauren Hong](https://arxiv.org/search/cs?searchtype=author&query=Hong,+L), [Runchu Tian](https://arxiv.org/search/cs?searchtype=author&query=Tian,+R), [Ruobing Xie](https://arxiv.org/search/cs?searchtype=author&query=Xie,+R), [Jie Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+J), [Mark Gerstein](https://arxiv.org/search/cs?searchtype=author&query=Gerstein,+M), [Dahai Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+D), [Zhiyuan Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z), [Maosong Sun](https://arxiv.org/search/cs?searchtype=author&query=Sun,+M)
View a PDF of the paper titled ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs, by Yujia Qin and 18 other authors
[View PDF](https://arxiv.org/pdf/2307.16789)
> Abstract:Despite the advancements of open-source large language models (LLMs), e.g., LLaMA, they remain significantly limited in tool-use capabilities, i.e., using external tools (APIs) to fulfill human instructions. The reason is that current instruction tuning largely focuses on basic language tasks but ignores the tool-use domain. This is in contrast to the excellent tool-use capabilities of state-of-the-art (SOTA) closed-source LLMs, e.g., ChatGPT. To bridge this gap, we introduce ToolLLM, a general tool-use framework encompassing data construction, model training, and evaluation. We first present ToolBench, an instruction-tuning dataset for tool use, which is constructed automatically using ChatGPT. Specifically, the construction can be divided into three stages: (i) API collection: we collect 16,464 real-world RESTful APIs spanning 49 categories from RapidAPI Hub; (ii) instruction generation: we prompt ChatGPT to generate diverse instructions involving these APIs, covering both single-tool and multi-tool scenarios; (iii) solution path annotation: we use ChatGPT to search for a valid solution path (chain of API calls) for each instruction. To enhance the reasoning capabilities of LLMs, we develop a novel depth-first search-based decision tree algorithm. It enables LLMs to evaluate multiple reasoning traces and expand the search space. Moreover, to evaluate the tool-use capabilities of LLMs, we develop an automatic evaluator: ToolEval. Based on ToolBench, we fine-tune LLaMA to obtain an LLM ToolLLaMA, and equip it with a neural API retriever to recommend appropriate APIs for each instruction. Experiments show that ToolLLaMA demonstrates a remarkable ability to execute complex instructions and generalize to unseen APIs, and exhibits comparable performance to ChatGPT. Our ToolLLaMA also demonstrates strong zero-shot generalization ability in an out-of-distribution tool-use dataset: APIBench.   
| Subjects:  |  Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)  |  
| --- | --- |  
| Cite as:  | [arXiv:2307.16789](https://arxiv.org/abs/2307.16789) [cs.AI]  |  
|   | (or  [arXiv:2307.16789v2](https://arxiv.org/abs/2307.16789v2) [cs.AI] for this version)   |  
|   |  <https://doi.org/10.48550/arXiv.2307.16789> Focus to learn more  |  
## Submission history
From: Yujia Qin [[view email](https://arxiv.org/show-email/85e4ecb2/2307.16789)]   
**[[v1]](https://arxiv.org/abs/2307.16789v1)** Mon, 31 Jul 2023 15:56:53 UTC (1,473 KB)  
**[v2]** Tue, 3 Oct 2023 14:45:48 UTC (1,477 KB)  

Full-text links:
## Access Paper:
View a PDF of the paper titled ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs, by Yujia Qin and 18 other authors
  * [View PDF](https://arxiv.org/pdf/2307.16789)
  * [TeX Source ](https://arxiv.org/src/2307.16789)


[view license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/ "Rights to this article")
### Current browse context:
cs.AI
[< prev](https://arxiv.org/prevnext?id=2307.16789&function=prev&context=cs.AI "previous in cs.AI \(accesskey p\)") |  [next >](https://arxiv.org/prevnext?id=2307.16789&function=next&context=cs.AI "next in cs.AI \(accesskey n\)")   

[new](https://arxiv.org/list/cs.AI/new) |  [recent](https://arxiv.org/list/cs.AI/recent) | [2023-07](https://arxiv.org/list/cs.AI/2023-07)
Change to browse by: 
[cs](https://arxiv.org/abs/2307.16789?context=cs)  
[cs.CL](https://arxiv.org/abs/2307.16789?context=cs.CL)  
[cs.LG](https://arxiv.org/abs/2307.16789?context=cs.LG)  

### References & Citations
  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2307.16789)
  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2307.16789)
  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2307.16789)


export BibTeX citation Loading...
## BibTeX formatted citation
×
loading...
Data provided by: 
### Bookmark
[ ![BibSonomy](https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png) ](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2307.16789&description=ToolLLM:%20Facilitating%20Large%20Language%20Models%20to%20Master%2016000+%20Real-world%20APIs "Bookmark on BibSonomy") [ ![Reddit](https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png) ](https://reddit.com/submit?url=https://arxiv.org/abs/2307.16789&title=ToolLLM:%20Facilitating%20Large%20Language%20Models%20to%20Master%2016000+%20Real-world%20APIs "Bookmark on Reddit")
Bibliographic Tools
# Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer _([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))_
Connected Papers Toggle
Connected Papers _([What is Connected Papers?](https://www.connectedpapers.com/about))_
Litmaps Toggle
Litmaps _([What is Litmaps?](https://www.litmaps.co/))_
scite.ai Toggle
scite Smart Citations _([What are Smart Citations?](https://www.scite.ai/))_
Code, Data, Media
# Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv _([What is alphaXiv?](https://alphaxiv.org/))_
Links to Code Toggle
CatalyzeX Code Finder for Papers _([What is CatalyzeX?](https://www.catalyzex.com))_
DagsHub Toggle
DagsHub _([What is DagsHub?](https://dagshub.com/))_
GotitPub Toggle
Gotit.pub _([What is GotitPub?](http://gotit.pub/faq))_
Huggingface Toggle
Hugging Face _([What is Huggingface?](https://huggingface.co/huggingface))_
ScienceCast Toggle
ScienceCast _([What is ScienceCast?](https://sciencecast.org/welcome))_
Demos
# Demos
Replicate Toggle
Replicate _([What is Replicate?](https://replicate.com/docs/arxiv/about))_
Spaces Toggle
Hugging Face Spaces _([What is Spaces?](https://huggingface.co/docs/hub/spaces))_
Spaces Toggle
TXYZ.AI _([What is TXYZ.AI?](https://txyz.ai))_
Related Papers
# Recommenders and Search Tools
Link to Influence Flower
Influence Flower _([What are Influence Flowers?](https://influencemap.cmlab.dev/))_
Core recommender toggle
CORE Recommender _([What is CORE?](https://core.ac.uk/services/recommender))_
  * Author
  * Venue
  * Institution
  * Topic


About arXivLabs 
# arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? [**Learn more about arXivLabs**](https://info.arxiv.org/labs/index.html).
[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2307.16789) | [Disable MathJax](javascript:setMathjaxCookie\(\)) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html)) 
  * [About](https://info.arxiv.org/about)
  * [Help](https://info.arxiv.org/help)


  * contact arXiv Click here to contact arXiv [ Contact](https://info.arxiv.org/help/contact.html)
  * subscribe to arXiv mailings Click here to subscribe [ Subscribe](https://info.arxiv.org/help/subscribe)


  * [Copyright](https://info.arxiv.org/help/license/index.html)
  * [Privacy Policy](https://info.arxiv.org/help/policies/privacy_policy.html)


  * [Web Accessibility Assistance](https://info.arxiv.org/help/web_accessibility.html)
  * [arXiv Operational Status ](https://status.arxiv.org)  



