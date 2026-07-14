[Jump to content](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#bodyContent)
Main menu
Main menu
move to sidebar hide
Navigation 
  * [Main page](https://en.wikipedia.org/wiki/Main_Page "Visit the main page \[z\]")
  * [Contents](https://en.wikipedia.org/wiki/Wikipedia:Contents "Guides to browsing Wikipedia")
  * [Current events](https://en.wikipedia.org/wiki/Portal:Current_events "Articles related to current events")
  * [Random article](https://en.wikipedia.org/wiki/Special:Random "Visit a randomly selected article \[x\]")
  * [About Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:About "Learn about Wikipedia and how it works")
  * [Contact us](https://en.wikipedia.org/wiki/Wikipedia:Contact_us "How to contact Wikipedia")


Contribute 
  * [Help](https://en.wikipedia.org/wiki/Help:Contents "Guidance on how to use and edit Wikipedia")
  * [Learn to edit](https://en.wikipedia.org/wiki/Help:Introduction "Learn how to edit Wikipedia")
  * [Community portal](https://en.wikipedia.org/wiki/Wikipedia:Community_portal "The hub for editors")
  * [Recent changes](https://en.wikipedia.org/wiki/Special:RecentChanges "A list of recent changes to Wikipedia \[r\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_upload_wizard "Add images or other media for use on Wikipedia")
  * [Special pages](https://en.wikipedia.org/wiki/Special:SpecialPages "A list of all special pages \[q\]")


[ ![](https://en.wikipedia.org/static/images/icons/enwiki-25.svg) ![Wikipedia](https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg) ![The Free Encyclopedia](https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-tagline-en-25.svg) ](https://en.wikipedia.org/wiki/Main_Page)
[Search ](https://en.wikipedia.org/wiki/Special:Search "Search Wikipedia \[f\]")
Search
Appearance
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Retrieval-augmented+generation "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Retrieval-augmented+generation "You're encouraged to log in; however, it's not mandatory. \[o\]")


Personal tools
  * [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
  * [Create account](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Retrieval-augmented+generation "You are encouraged to create an account and log in; however, it is not mandatory")
  * [Log in](https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Retrieval-augmented+generation "You're encouraged to log in; however, it's not mandatory. \[o\]")


## Contents
move to sidebar hide
  * [ (Top) ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
  * [ 1 RAG and LLM limitations ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#RAG_and_LLM_limitations)
  * [ 2 Process ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Process) Toggle Process subsection
    * [ 2.1 RAG key stages ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#RAG_key_stages)
  * [ 3 Applications ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Applications)
  * [ 4 Improvements ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Improvements) Toggle Improvements subsection
    * [ 4.1 Encoder ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Encoder)
    * [ 4.2 Retriever-centric methods ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Retriever-centric_methods)
    * [ 4.3 Language model ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Language_model)
    * [ 4.4 Chunking ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Chunking)
    * [ 4.5 Hybrid search ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Hybrid_search)
  * [ 5 Challenges ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#Challenges) Toggle Challenges subsection
    * [ 5.1 RAG poisoning ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#RAG_poisoning)
  * [ 6 References ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#References)


Toggle the table of contents
# Retrieval-augmented generation
21 languages
  * [العربية](https://ar.wikipedia.org/wiki/%D8%AA%D9%88%D9%84%D9%8A%D8%AF_%D9%85%D8%B9%D8%B2%D8%B2_%D8%A8%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%AD%D8%B6%D8%A7%D8%B1 "توليد معزز بالاستحضار – Arabic")
  * [Bosanski](https://bs.wikipedia.org/wiki/Generiranje_pro%C5%A1ireno_pretra%C5%BEivanjem "Generiranje prošireno pretraživanjem – Bosnian")
  * [Català](https://ca.wikipedia.org/wiki/Generaci%C3%B3_amb_recuperaci%C3%B3_augmentada "Generació amb recuperació augmentada – Catalan")
  * [Čeština](https://cs.wikipedia.org/wiki/Retrieval-augmented_generation "Retrieval-augmented generation – Czech")
  * [Deutsch](https://de.wikipedia.org/wiki/Retrieval-Augmented_Generation "Retrieval-Augmented Generation – German")
  * [Español](https://es.wikipedia.org/wiki/Generaci%C3%B3n_aumentada_por_recuperaci%C3%B3n "Generación aumentada por recuperación – Spanish")
  * [Français](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ration_%C3%A0_enrichissement_contextuel "Génération à enrichissement contextuel – French")
  * [עברית](https://he.wikipedia.org/wiki/%D7%99%D7%A6%D7%99%D7%A8%D7%94_%D7%9E%D7%91%D7%95%D7%A1%D7%A1%D7%AA-%D7%A9%D7%9C%D7%99%D7%A4%D7%94 "יצירה מבוססת-שליפה – Hebrew")
  * [Bahasa Indonesia](https://id.wikipedia.org/wiki/Retrieval-augmented_generation "Retrieval-augmented generation – Indonesian")
  * [Italiano](https://it.wikipedia.org/wiki/Retrieval_augmented_generation "Retrieval augmented generation – Italian")
  * [日本語](https://ja.wikipedia.org/wiki/Retrieval-Augmented_Generation "Retrieval-Augmented Generation – Japanese")
  * [한국어](https://ko.wikipedia.org/wiki/%EA%B2%80%EC%83%89%EC%A6%9D%EA%B0%95%EC%83%9D%EC%84%B1 "검색증강생성 – Korean")
  * [Polski](https://pl.wikipedia.org/wiki/Retrieval-augmented_generation "Retrieval-augmented generation – Polish")
  * [Português](https://pt.wikipedia.org/wiki/Gera%C3%A7%C3%A3o_aumentada_por_recupera%C3%A7%C3%A3o "Geração aumentada por recuperação – Portuguese")
  * [Русский](https://ru.wikipedia.org/wiki/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D1%81_%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9_%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%BA%D0%BE%D0%B9 "Генерация с дополненной выборкой – Russian")
  * [Ślůnski](https://szl.wikipedia.org/wiki/RAG "RAG – Silesian")
  * [ไทย](https://th.wikipedia.org/wiki/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%AA%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%94%E0%B8%B6%E0%B8%87%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5 "การสร้างที่เสริมด้วยการดึงข้อมูล – Thai")
  * [Türkçe](https://tr.wikipedia.org/wiki/Eri%C5%9Fim_destekli_%C3%BCretim "Erişim destekli üretim – Turkish")
  * [Українська](https://uk.wikipedia.org/wiki/%D0%94%D0%BE%D0%BF%D0%BE%D0%B2%D0%BD%D0%B5%D0%BD%D0%B5_%D0%BF%D0%BE%D1%88%D1%83%D0%BA%D0%BE%D0%BC_%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F "Доповнене пошуком генерування – Ukrainian")
  * [Tiếng Việt](https://vi.wikipedia.org/wiki/T%E1%BA%A1o_sinh_d%E1%BB%B1a_tr%C3%AAn_truy_xu%E1%BA%A5t_t%C4%83ng_c%C6%B0%E1%BB%9Dng "Tạo sinh dựa trên truy xuất tăng cường – Vietnamese")
  * [中文](https://zh.wikipedia.org/wiki/%E6%AA%A2%E7%B4%A2%E5%A2%9E%E5%BC%B7%E7%94%9F%E6%88%90 "檢索增強生成 – Chinese")


[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q121362277#sitelinks-wikipedia "Edit interlanguage links")
  * [Article](https://en.wikipedia.org/wiki/Retrieval-augmented_generation "View the content page \[c\]")
  * [Talk](https://en.wikipedia.org/wiki/Talk:Retrieval-augmented_generation "Discuss improvements to the content page \[t\]")


English
  * [Read](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
  * [Edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=history "Past revisions of this page \[h\]")


Tools
Tools
move to sidebar hide
Actions 
  * [Read](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
  * [Edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit "Edit this page \[e\]")
  * [View history](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=history)


General 
  * [What links here](https://en.wikipedia.org/wiki/Special:WhatLinksHere/Retrieval-augmented_generation "List of all English Wikipedia pages containing links to this page \[j\]")
  * [Related changes](https://en.wikipedia.org/wiki/Special:RecentChangesLinked/Retrieval-augmented_generation "Recent changes in pages linked from this page \[k\]")
  * [Upload file](https://en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files \[u\]")
  * [Permanent link](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&oldid=1357460039 "Permanent link to this revision of this page")
  * [Page information](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=info "More information about this page")
  * [Cite this page](https://en.wikipedia.org/w/index.php?title=Special:CiteThisPage&page=Retrieval-augmented_generation&id=1357460039&wpFormIdentifier=titleform "Information on how to cite this page")
  * [Get shortened URL](https://en.wikipedia.org/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRetrieval-augmented_generation)


Print/export 
  * [Download as PDF](https://en.wikipedia.org/w/index.php?title=Special:DownloadAsPdf&page=Retrieval-augmented_generation&action=show-download-screen "Download this page as a PDF file")
  * [Printable version](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&printable=yes "Printable version of this page \[p\]")


In other projects 
  * [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Retrieval-augmented_generation)
  * [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q121362277 "Structured data on this page hosted by Wikidata \[g\]")


Appearance
move to sidebar hide
From Wikipedia, the free encyclopedia
Type of information retrieval using LLMs
**Retrieval-augmented generation** (**RAG**) is a technique that enables [large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") (LLMs) to retrieve and incorporate new information from external data sources.[[1]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-IBM-2023-1) With RAG, LLMs first refer to a specified set of documents, then respond to user queries. These documents supplement information from the LLM's pre-existing [training data](https://en.wikipedia.org/wiki/Training_data "Training data").[[2]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-MIT_Technology_Review-2024-2) This allows LLMs to use domain-specific and/or updated information that is not available in the training data.[[2]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-MIT_Technology_Review-2024-2) For example, this enables LLM-based [chatbots](https://en.wikipedia.org/wiki/Chatbot "Chatbot") to access internal company data or generate responses based on authoritative sources. 
RAG improves LLMs by incorporating [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval "Information retrieval") before generating responses.[[3]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-BUZBP-3) Unlike LLMs that rely on static training data, RAG pulls relevant text from databases, uploaded documents, or web sources.[[1]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-IBM-2023-1) According to _[Ars Technica](https://en.wikipedia.org/wiki/Ars_Technica "Ars Technica")_ , "RAG is a way of improving LLM performance, in essence by blending the LLM process with a web search or other document look-up process to help LLMs stick to the facts." This method helps reduce [AI hallucinations](https://en.wikipedia.org/wiki/AI_hallucinations "AI hallucinations"),[[3]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-BUZBP-3) which have caused chatbots to describe policies that don't exist, or recommend nonexistent legal cases to lawyers that are looking for citations to support their arguments.[[4]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-Ars_Technica-2024-4)
RAG also reduces the need to retrain LLMs with new data, saving on computational and financial costs.[[1]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-IBM-2023-1) Beyond efficiency gains, RAG also allows LLMs to include sources in their responses, so users can verify the cited sources. This provides greater transparency, as users can cross-check retrieved content to ensure accuracy and relevance. 
The term retrieval-augmented generation (RAG) was introduced in a 2020 paper that described combining a parametric language model with a non-parametric external memory accessed through retrieval at inference time.[[3]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-BUZBP-3)
## RAG and LLM limitations
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=1 "Edit section: RAG and LLM limitations")]
LLMs can provide incorrect information. For example, when Google first demonstrated its LLM tool "[Google Bard](https://en.wikipedia.org/wiki/Google_Bard "Google Bard")" (later re-branded to Gemini), the LLM provided incorrect information about the [James Webb Space Telescope](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope "James Webb Space Telescope"). This error contributed to a $100 billion decline in [Google's](https://en.wikipedia.org/wiki/Alphabet_Inc. "Alphabet Inc.") stock value.[[4]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-Ars_Technica-2024-4) RAG is used to prevent these errors, but it does not solve all the problems. For example, LLMs can generate misinformation even when pulling from factually correct sources if they misinterpret the context. _[MIT Technology Review](https://en.wikipedia.org/wiki/MIT_Technology_Review "MIT Technology Review")_ gives the example of an AI-generated response stating, "The United States has had one Muslim president, Barack Hussein Obama." The model retrieved this from an academic book rhetorically titled _Barack Hussein Obama: America's First Muslim President?_ The LLM did not "know" or "understand" the context of the title, generating a false statement.[[2]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-MIT_Technology_Review-2024-2)
LLMs with RAG are programmed to prioritize new information. This technique has been called "prompt stuffing." Without prompt stuffing, the LLM's input is generated by a user; with prompt stuffing, additional relevant context is added to this input to guide the model's response. This approach provides the LLM with key information early in the prompt, encouraging it to prioritize the supplied data over pre-existing training knowledge.[[5]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-5)
## Process
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=2 "Edit section: Process")]
Retrieval-augmented generation (RAG) enhances [large language models](https://en.wikipedia.org/wiki/Large_language_model "Large language model") (LLMs) by incorporating an [information-retrieval](https://en.wikipedia.org/wiki/Information_retrieval "Information retrieval") mechanism that allows models to access and utilize additional data beyond their original training set. _[Ars Technica](https://en.wikipedia.org/wiki/Ars_Technica "Ars Technica")_ notes that "when new information becomes available, rather than having to retrain the model, all that's needed is to augment the model's external knowledge base with the updated information" ("augmentation").[[4]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-Ars_Technica-2024-4) IBM states that "in the generative phase, the LLM draws from the augmented prompt and its internal representation of its training data to synthesize" an answer.[[1]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-IBM-2023-1)
### RAG key stages
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=3 "Edit section: RAG key stages")]
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/RAG_diagram.svg/250px-RAG_diagram.svg.png)](https://en.wikipedia.org/wiki/File:RAG_diagram.svg)Overview of RAG process, combining external documents and user input into an LLM prompt to get tailored output
Typically, the data to be referenced is converted into LLM [embeddings](https://en.wikipedia.org/wiki/Word_embeddings "Word embeddings"), numerical representations in the form of a large vector space. RAG can be used on unstructured (usually text), semi-structured, or structured data (for example [knowledge graphs](https://en.wikipedia.org/wiki/Knowledge_graphs "Knowledge graphs")). These embeddings are then stored in a [vector database](https://en.wikipedia.org/wiki/Vector_database "Vector database") to allow for [document retrieval](https://en.wikipedia.org/wiki/Document_retrieval "Document retrieval"). 
Given a user query, a document retriever is first called to select the most relevant documents that will be used to augment the query.[[2]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-MIT_Technology_Review-2024-2)[[3]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-BUZBP-3) This comparison can be done using a variety of methods, which depend in part on the type of indexing used.[[1]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-IBM-2023-1)
The model feeds this relevant retrieved information into the LLM via [prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering") of the user's original query. Newer implementations (as of 2023[[update]](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit)) can also incorporate specific augmentation modules with abilities such as expanding queries into multiple domains and using memory and self-improvement to learn from previous retrievals. 
Finally, the LLM can generate output based on both the query and the retrieved documents.[[2]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-MIT_Technology_Review-2024-2)[[3]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-BUZBP-3) Some models incorporate extra steps to improve output, such as the re-ranking of retrieved information, context selection, and [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\) "Fine-tuning \(deep learning\)"). 
## Applications
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=4 "Edit section: Applications")]
Retrieval-augmented generation is used in applications where generated responses need to be grounded in external or frequently updated information.[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]
In healthcare, RAG has been studied as a way to ground large language model outputs in external medical knowledge sources, although reviews have noted continuing challenges around evaluation, ethics, and clinical reliability.[[6]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-6)
## Improvements
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=5 "Edit section: Improvements")]
Improvements to the basic process above can be applied at different stages in the RAG flow. 
### Encoder
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=6 "Edit section: Encoder")]
These methods focus on the encoding of text as either dense or sparse vectors. [Sparse vectors](https://en.wikipedia.org/wiki/Sparse_vector "Sparse vector"), which encode the identity of a word, are typically [dictionary](https://en.wikipedia.org/wiki/Large_language_model#Tokenization "Large language model")-length and contain mostly zeros. [Dense vectors](https://en.wikipedia.org/wiki/Dense_matrix "Dense matrix"), which encode meaning, are more compact and contain fewer zeros. Various enhancements can improve the way similarities are calculated in the vector stores (databases).[[7]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-Luan-2021-7)
  * Performance improves by optimizing how vector similarities are calculated. [Dot products](https://en.wikipedia.org/wiki/Dot_product "Dot product") enhance similarity scoring, while [approximate nearest neighbor](https://en.wikipedia.org/wiki/Approximate_nearest_neighbor_search "Approximate nearest neighbor search") (ANN) searches improve retrieval efficiency over [K-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm "K-nearest neighbors algorithm") (KNN) searches.[[8]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-8)
  * Accuracy may be improved with Late Interactions, which allow the system to compare words more precisely after retrieval. This helps refine document ranking and improve search relevance.[[9]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-colbert-9)
  * Hybrid vector approaches may be used to combine dense vector representations with sparse [one-hot](https://en.wikipedia.org/wiki/One-hot "One-hot") vectors, taking advantage of the computational efficiency of sparse dot products over dense vector operations.[[7]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-Luan-2021-7)
  * Other retrieval techniques focus on improving accuracy by refining how documents are selected. Some retrieval methods combine sparse representations, such as SPLADE, with query expansion strategies to improve search accuracy and recall.[[10]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-10)


### Retriever-centric methods
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=7 "Edit section: Retriever-centric methods")]
These methods aim to enhance the quality of document retrieval in vector databases: 
  * Pre-training the retriever using the _Inverse Cloze Task_ (ICT), a technique that helps the model learn retrieval patterns by predicting masked text within documents.[[11]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-orqa-11)
  * Supervised retriever optimization aligns retrieval probabilities with the generator model's likelihood distribution. This involves retrieving the top-k vectors for a given prompt, scoring the generated response's [perplexity](https://en.wikipedia.org/wiki/Perplexity "Perplexity"), and minimizing [KL divergence](https://en.wikipedia.org/wiki/KL_divergence "KL divergence") between the retriever's selections and the model's likelihoods to refine retrieval.[[12]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-12)
  * Reranking techniques can refine retriever performance by prioritizing the most relevant retrieved documents during training.[[13]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-13)


### Language model
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=8 "Edit section: Language model")]
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Language_model_in_Deepmind%27s_2021_Retro_for_RAG.svg/330px-Language_model_in_Deepmind%27s_2021_Retro_for_RAG.svg.png)](https://en.wikipedia.org/wiki/File:Language_model_in_Deepmind%27s_2021_Retro_for_RAG.svg)
Retro language model for RAG. Each Retro block consists of Attention, Chunked Cross Attention, and Feed Forward layers. Black-lettered boxes show data being changed, and blue lettering shows the algorithm performing the changes.
By redesigning the language model with the retriever in mind, a 25-time smaller network can get comparable perplexity as its much larger counterparts.[[14]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-borgeaud-14) Because it is trained from scratch, this method (Retro) incurs the high cost of training runs that the original RAG scheme avoided. The hypothesis is that by giving domain knowledge during training, Retro needs less focus on the domain and can devote its smaller weight resources only to language semantics. The redesigned language model is shown here. 
It has been reported that Retro is not reproducible, so modifications were made to make it so. The more reproducible version is called Retro++ and includes in-context RAG.[[15]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-wang2023a-15)
### Chunking
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=9 "Edit section: Chunking")]
See also: [Chunking (computing)](https://en.wikipedia.org/wiki/Chunking_\(computing\) "Chunking \(computing\)")
Chunking involves various strategies for breaking up the data into vectors so the retriever can find details in it. 
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Rag-doc-styles.png/500px-Rag-doc-styles.png)](https://en.wikipedia.org/wiki/File:Rag-doc-styles.png)
Different data styles have patterns that correct chunking can take advantage of.
Three types of chunking strategies are:[_[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]
  * Fixed length with overlap. This is fast and easy. Overlapping consecutive chunks helps to maintain semantic context across chunks.
  * Syntax-based chunks can break the document up into sentences. Libraries such as [spaCy](https://en.wikipedia.org/wiki/SpaCy "SpaCy") or [NLTK](https://en.wikipedia.org/wiki/Natural_Language_Toolkit "Natural Language Toolkit") can also help.
  * File format-based chunking. Certain file types have natural chunks built in, and it's best to respect them. For example, code files are best chunked and vectorized as whole functions or classes. HTML files should leave <table> or base64 encoded <img> elements intact. Similar considerations should be taken for pdf files. Libraries such as Unstructured or [LangChain](https://en.wikipedia.org/wiki/LangChain "LangChain") can assist with this method.


### Hybrid search
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=10 "Edit section: Hybrid search")]
Sometimes vector database searches can miss key facts needed to answer a user's question. One way to mitigate this is to do a traditional text search, add those results to the text chunks linked to the retrieved vectors from the vector search, and feed the combined hybrid text into the language model for generation.[[16]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-16)
## Challenges
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=11 "Edit section: Challenges")]
RAG does not prevent hallucinations in LLMs. According to _[Ars Technica](https://en.wikipedia.org/wiki/Ars_Technica "Ars Technica")_ , "It is not a direct solution because the LLM can still hallucinate around the source material in its response."[[4]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-Ars_Technica-2024-4)
While RAG improves the accuracy of large language models (LLMs), it does not eliminate all challenges. One limitation is that while RAG reduces the need for frequent model retraining, it does not remove it entirely. Additionally, LLMs may struggle to recognize when they lack sufficient information to provide a reliable response. Without specific training, models may generate answers even when they should indicate uncertainty. According to [IBM](https://en.wikipedia.org/wiki/IBM "IBM"), this issue can arise when the model lacks the ability to assess its own knowledge limitations.[[1]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-IBM-2023-1)
### RAG poisoning
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=12 "Edit section: RAG poisoning")]
RAG systems may retrieve factually correct but misleading sources, leading to errors in interpretation. In some cases, an LLM may extract statements from a source without considering its context, resulting in an incorrect conclusion. Additionally, when faced with conflicting information, RAG models may struggle to determine which source is accurate. The worst case outcome of this limitation is that the model may combine details from multiple sources producing responses that merge outdated and updated information in a misleading manner. According to the _[MIT Technology Review](https://en.wikipedia.org/wiki/MIT_Technology_Review "MIT Technology Review")_ , these issues occur because RAG systems may misinterpret the data they retrieve.[[2]](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_note-MIT_Technology_Review-2024-2)
## References
[[edit](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&action=edit&section=13 "Edit section: References")]
  1. ^ [_**a**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-IBM-2023_1-0) [_**b**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-IBM-2023_1-1) [_**c**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-IBM-2023_1-2) [_**d**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-IBM-2023_1-3) [_**e**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-IBM-2023_1-4) [_**f**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-IBM-2023_1-5) ["What is retrieval-augmented generation?"](https://research.ibm.com/blog/retrieval-augmented-generation-RAG). _IBM_. 22 August 2023. Retrieved 7 March 2025.
  2. ^ [_**a**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-MIT_Technology_Review-2024_2-0) [_**b**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-MIT_Technology_Review-2024_2-1) [_**c**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-MIT_Technology_Review-2024_2-2) [_**d**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-MIT_Technology_Review-2024_2-3) [_**e**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-MIT_Technology_Review-2024_2-4) [_**f**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-MIT_Technology_Review-2024_2-5) ["Why Google's AI Overviews gets things wrong"](https://www.technologyreview.com/2024/05/31/1093019/why-are-googles-ai-overviews-results-so-bad/). _MIT Technology Review_. 31 May 2024. Retrieved 7 March 2025.
  3. ^ [_**a**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-BUZBP_3-0) [_**b**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-BUZBP_3-1) [_**c**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-BUZBP_3-2) [_**d**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-BUZBP_3-3) [_**e**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-BUZBP_3-4) Lewis, Patrick; Perez, Ethan; Piktus, Aleksandra; Petroni, Fabio; Karpukhin, Vladimir; Goyal, Naman; Küttler, Heinrich; Lewis, Mike; Yih, Wen-tau; Rocktäschel, Tim; Riedel, Sebastian; Kiela, Douwe (2020). ["Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html). _Advances in Neural Information Processing Systems_. **33**. Curran Associates, Inc.: 9459–9474. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2005.11401](https://arxiv.org/abs/2005.11401).
  4. ^ [_**a**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-Ars_Technica-2024_4-0) [_**b**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-Ars_Technica-2024_4-1) [_**c**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-Ars_Technica-2024_4-2) [_**d**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-Ars_Technica-2024_4-3) ["Can a technology called RAG keep AI models from making stuff up?"](https://arstechnica.com/ai/2024/06/can-a-technology-called-rag-keep-ai-models-from-making-stuff-up/). _Ars Technica_. 6 June 2024. Retrieved 7 March 2025.
  5. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-5)** ["Mitigating LLM hallucinations in text summarisation"](https://www.bbc.co.uk/rd/articles/2024-06-mitigating-llm-hallucinations-in-text-summarisation). _BBC_. 20 June 2024. Retrieved 7 March 2025.
  6. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-6)** Amugongo, Lameck Mbangula; Mascheroni, Pietro; Brooks, Steven; Doering, Stefan; Seidel, Jan (2025-06-11). ["Retrieval augmented generation for large language models in healthcare: A systematic review"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12157099). _PLOS Digital Health_. **4** (6) e0000877. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1371/journal.pdig.0000877](https://doi.org/10.1371%2Fjournal.pdig.0000877). [PMC](https://en.wikipedia.org/wiki/PMC_\(identifier\) "PMC \(identifier\)") [12157099](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12157099).
  7. ^ [_**a**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-Luan-2021_7-0) [_**b**_](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-Luan-2021_7-1) Luan, Yi; Eisenstein, Jacob; Toutanova, Kristina; Collins, Michael (26 April 2021). ["Sparse, Dense, and Attentional Representations for Text Retrieval"](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00369/100684/Sparse-Dense-and-Attentional-Representations-for). _Transactions of the Association for Computational Linguistics_. **9** : 329–345. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2005.00181](https://arxiv.org/abs/2005.00181). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1162/tacl_a_00369](https://doi.org/10.1162%2Ftacl_a_00369). Retrieved 15 March 2025.
  8. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-8)** ["Information retrieval"](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval). _Microsoft_. 10 January 2025. Retrieved 15 March 2025.
  9. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-colbert_9-0)** Khattab, Omar; Zaharia, Matei (2020). ["ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT"](https://dl.acm.org/doi/10.1145/3397271.3401075). _Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval_. pp. 39–48. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/3397271.3401075](https://doi.org/10.1145%2F3397271.3401075). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN \(identifier\)") [978-1-4503-8016-4](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4503-8016-4 "Special:BookSources/978-1-4503-8016-4").
  10. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-10)** Wang, Yup; Conroy, John M.; Molino, Neil; Yang, Julia; Green, Mike (2024). ["Laboratory for Analytic Sciences in TREC 2024 Retrieval Augmented Generation Track"](https://trec.nist.gov/pubs/trec33/index.html). _NIST TREC 2024_. Retrieved 15 March 2025.
  11. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-orqa_11-0)** Lee, Kenton; Chang, Ming-Wei; Toutanova, Kristina (2019). ["](https://aclanthology.org/P19-1612.pdf) (PDF).
  12. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-12)** Shi, Weijia; Min, Sewon; Yasunaga, Michihiro; Seo, Minjoon; James, Rich; Lewis, Mike; Zettlemoyer, Luke; Yih, Wen-tau (June 2024). ["REPLUG: Retrieval-Augmented Black-Box Language Models"](https://aclanthology.org/2024.naacl-long.463/). _Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)_. pp. 8371–8384. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2301.12652](https://arxiv.org/abs/2301.12652). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/2024.naacl-long.463](https://doi.org/10.18653%2Fv1%2F2024.naacl-long.463). Retrieved 16 March 2025.
  13. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-13)** Ram, Ori; Levine, Yoav; Dalmedigos, Itay; Muhlgay, Dor; Shashua, Amnon; Leyton-Brown, Kevin; Shoham, Yoav (2023). ["In-Context Retrieval-Augmented Language Models"](https://aclanthology.org/2023.tacl-1.75/). _Transactions of the Association for Computational Linguistics_. **11** : 1316–1331. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2302.00083](https://arxiv.org/abs/2302.00083). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1162/tacl_a_00605](https://doi.org/10.1162%2Ftacl_a_00605). Retrieved 16 March 2025.
  14. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-borgeaud_14-0)** Borgeaud, Sebastian; Mensch, Arthur (2021). ["Improving language models by retrieving from trillions of tokens"](https://proceedings.mlr.press/v162/borgeaud22a/borgeaud22a.pdf) (PDF).
  15. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-wang2023a_15-0)** Wang, Boxin; Ping, Wei; Xu, Peng; McAfee, Lawrence; Liu, Zihan; Shoeybi, Mohammad; Dong, Yi; Kuchaiev, Oleksii; Li, Bo; Xiao, Chaowei; Anandkumar, Anima; Catanzaro, Bryan (2023). ["Shall We Pretrain Autoregressive Language Models with Retrieval? A Comprehensive Study"](https://aclanthology.org/2023.emnlp-main.482/). _Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing_. pp. 7763–7786. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.18653/v1/2023.emnlp-main.482](https://doi.org/10.18653%2Fv1%2F2023.emnlp-main.482).
  16. **[^](https://en.wikipedia.org/wiki/Retrieval-augmented_generation#cite_ref-16)** Bruch, Sebastian; Gai, Siyu; Ingber, Amir (2023). "An Analysis of Fusion Functions for Hybrid Retrieval". _ACM Transactions on Information Systems_. **42** (1): 1–35. [arXiv](https://en.wikipedia.org/wiki/ArXiv_\(identifier\) "ArXiv \(identifier\)"):[2210.11934](https://arxiv.org/abs/2210.11934). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi \(identifier\)"):[10.1145/3596512](https://doi.org/10.1145%2F3596512).

  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Generative_AI "Template:Generative AI")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Generative_AI "Template talk:Generative AI")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Generative_AI "Special:EditPage/Template:Generative AI")

[Generative AI](https://en.wikipedia.org/wiki/Generative_AI "Generative AI")  |  
| --- |  
| Concepts  | 
  * [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder "Autoencoder")
  * [Deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning")
  * [Fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\) "Fine-tuning \(deep learning\)")
  * [Foundation model](https://en.wikipedia.org/wiki/Foundation_model "Foundation model")
  * [Generative adversarial network](https://en.wikipedia.org/wiki/Generative_adversarial_network "Generative adversarial network")
  * [Generative pre-trained transformer](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
  * [Large language model](https://en.wikipedia.org/wiki/Large_language_model "Large language model")
  * [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol "Model Context Protocol")
  * [Neural network](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\) "Neural network \(machine learning\)")
  * [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering")
  * [Reinforcement learning from human feedback](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")
  * Retrieval-augmented generation
  * [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning")
  * [Stochastic parrot](https://en.wikipedia.org/wiki/Stochastic_parrot "Stochastic parrot")
  * [Synthetic data](https://en.wikipedia.org/wiki/Synthetic_data "Synthetic data")
  * [Top-p sampling](https://en.wikipedia.org/wiki/Top-p_sampling "Top-p sampling")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning\) "Transformer \(deep learning\)")
  * [Variational autoencoder](https://en.wikipedia.org/wiki/Variational_autoencoder "Variational autoencoder")
  * [Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding "Vibe coding")
  * [Vision transformer](https://en.wikipedia.org/wiki/Vision_transformer "Vision transformer")
  * [Word embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding")

 |  
| Models  |   
 | Text  | 
  * [Amazon Nova](https://en.wikipedia.org/wiki/Amazon_Nova "Amazon Nova")
  * [Character.ai](https://en.wikipedia.org/wiki/Character.ai "Character.ai")
  * [Claude](https://en.wikipedia.org/wiki/Claude_\(language_model\) "Claude \(language model\)")
  * [Command](https://en.wikipedia.org/wiki/Cohere#Products "Cohere")
  * [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek_\(chatbot\) "DeepSeek \(chatbot\)")
  * [Doubao](https://en.wikipedia.org/wiki/Doubao "Doubao")
  * [Ernie](https://en.wikipedia.org/wiki/Ernie_Bot "Ernie Bot")
  * [EXAONE](https://en.wikipedia.org/wiki/ESTsoft#Government_project_K-EXAONE "ESTsoft")
  * [Gemini](https://en.wikipedia.org/wiki/Google_Gemini "Google Gemini")
  * [Gemma](https://en.wikipedia.org/wiki/Gemma_\(language_model\) "Gemma \(language model\)")
  * [GLM](https://en.wikipedia.org/wiki/Z.ai#History "Z.ai")
  * [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer "Generative pre-trained transformer")
    * [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT "ChatGPT")
  * [Grok](https://en.wikipedia.org/wiki/Grok_\(chatbot\) "Grok \(chatbot\)")
  * [IBM Granite](https://en.wikipedia.org/wiki/IBM_Granite "IBM Granite")
  * [Kimi](https://en.wikipedia.org/wiki/Kimi_\(chatbot\) "Kimi \(chatbot\)")
  * [MAI](https://en.wikipedia.org/wiki/Microsoft_AI#History "Microsoft AI")
  * [Microsoft Copilot](https://en.wikipedia.org/wiki/Microsoft_Copilot "Microsoft Copilot")
  * [Mistral](https://en.wikipedia.org/wiki/Mistral_AI#Models "Mistral AI")
  * [MiniMax](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")
  * [Muse Spark](https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs#Models "Meta Superintelligence Labs")
  * [Nemotron](https://en.wikipedia.org/wiki/Nemotron "Nemotron")
  * [Perplexity](https://en.wikipedia.org/wiki/Perplexity_AI "Perplexity AI")
  * [Solar](https://en.wikipedia.org/wiki/Upstage_\(company\)#Models "Upstage \(company\)")
  * [Poe](https://en.wikipedia.org/wiki/Quora#Poe "Quora")
  * [HKChat](https://en.wikipedia.org/wiki/HKChat "HKChat")
  * [Qwen](https://en.wikipedia.org/wiki/Qwen "Qwen")
  * [Tencent Hy](https://en.wikipedia.org/wiki/Tencent#2021%E2%80%93present:_Regulatory_scrutiny "Tencent")
  * [Xiaomi MiMo](https://en.wikipedia.org/wiki/Xiaomi_MiMo "Xiaomi MiMo")
  * [You.com](https://en.wikipedia.org/wiki/You.com "You.com")

 |  
| --- | --- |  
| [Image](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model")  | 
  * [Adobe Firefly](https://en.wikipedia.org/wiki/Adobe_Firefly "Adobe Firefly")
  * [Flux](https://en.wikipedia.org/wiki/Flux_\(text-to-image_model\) "Flux \(text-to-image model\)")
  * [GPT Image](https://en.wikipedia.org/wiki/GPT_Image "GPT Image")
  * [Ideogram](https://en.wikipedia.org/wiki/Ideogram_\(text-to-image_model\) "Ideogram \(text-to-image model\)")
  * [Midjourney](https://en.wikipedia.org/wiki/Midjourney "Midjourney")
  * [Nano Banana](https://en.wikipedia.org/wiki/Nano_Banana "Nano Banana")
  * [Recraft](https://en.wikipedia.org/wiki/Recraft "Recraft")
  * [Seedream](https://en.wikipedia.org/wiki/ByteDance#Seedream "ByteDance")
  * [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion "Stable Diffusion")

 |  
| [Video](https://en.wikipedia.org/wiki/Text-to-video_model "Text-to-video model")  | 
  * [Dream Machine](https://en.wikipedia.org/wiki/Dream_Machine_\(text-to-video_model\) "Dream Machine \(text-to-video model\)")
  * [Genie](https://en.wikipedia.org/wiki/Genie_\(world_model\) "Genie \(world model\)")
    * [world model](https://en.wikipedia.org/wiki/World_model_\(artificial_intelligence\) "World model \(artificial intelligence\)")
  * [Hailuo AI](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Hailuo_AI "MiniMax \(company\)")
  * [Kling AI](https://en.wikipedia.org/wiki/Kling_AI "Kling AI")
  * [LTX](https://en.wikipedia.org/wiki/LTX_\(text-to-video_model\) "LTX \(text-to-video model\)")
  * [Runway Gen](https://en.wikipedia.org/wiki/Runway_\(company\)#Services_and_technologies "Runway \(company\)")
  * [Seedance](https://en.wikipedia.org/wiki/Seedance_2.0 "Seedance 2.0")
  * [Sora](https://en.wikipedia.org/wiki/Sora_\(text-to-video_model\) "Sora \(text-to-video model\)")
  * [Veo](https://en.wikipedia.org/wiki/Veo_\(text-to-video_model\) "Veo \(text-to-video model\)")

 |  
| [Speech](https://en.wikipedia.org/wiki/Speech_synthesis#Text-to-speech_systems "Speech synthesis")  | 
  * [15.ai](https://en.wikipedia.org/wiki/15.ai "15.ai")
  * [Eleven](https://en.wikipedia.org/wiki/ElevenLabs#Products "ElevenLabs")
  * [Gemini Speech](https://en.wikipedia.org/wiki/Gemini_\(language_model\) "Gemini \(language model\)")
  * [MiniMax Speech](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")

 |  
| [Music](https://en.wikipedia.org/wiki/Artificial_intelligence_in_music "Artificial intelligence in music")  | 
  * [Eleven Music](https://en.wikipedia.org/wiki/ElevenLabs#Products "ElevenLabs")
  * [Endel](https://en.wikipedia.org/wiki/Endel_\(app\) "Endel \(app\)")
  * [MiniMax Music](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")
  * [Riffusion](https://en.wikipedia.org/wiki/Riffusion "Riffusion")
  * [Suno](https://en.wikipedia.org/wiki/Suno_\(platform\) "Suno \(platform\)")
  * [Udio](https://en.wikipedia.org/wiki/Udio "Udio")

 |  
 |  
| Products  |   
 | [Coding tools](https://en.wikipedia.org/wiki/List_of_AI-assisted_software_development_tools "List of AI-assisted software development tools")  | 
  * [Claude Code](https://en.wikipedia.org/wiki/Claude_Code "Claude Code")
  * [Codex](https://en.wikipedia.org/wiki/Codex_\(AI_agent\) "Codex \(AI agent\)")
  * [Cursor](https://en.wikipedia.org/wiki/Cursor_\(code_editor\) "Cursor \(code editor\)")
  * [Devin AI](https://en.wikipedia.org/wiki/Devin_AI "Devin AI")
  * [GitHub Copilot](https://en.wikipedia.org/wiki/GitHub_Copilot "GitHub Copilot")
  * [Google Antigravity](https://en.wikipedia.org/wiki/Google_Antigravity "Google Antigravity")
  * [Replit](https://en.wikipedia.org/wiki/Replit "Replit")

 |  
| --- | --- |  
| [Agents](https://en.wikipedia.org/wiki/AI_agent "AI agent")  | 
  * [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT "AutoGPT")
  * [ChatGPT agent](https://en.wikipedia.org/wiki/ChatGPT_agent "ChatGPT agent")
  * [Claude Cowork](https://en.wikipedia.org/wiki/Claude_Cowork "Claude Cowork")
  * [Gemini Spark](https://en.wikipedia.org/wiki/Gemini_Spark "Gemini Spark")
  * [Manus](https://en.wikipedia.org/wiki/Manus_\(AI_agent\) "Manus \(AI agent\)")
  * [MiniMax Agent](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Technology "MiniMax \(company\)")
  * [OpenClaw](https://en.wikipedia.org/wiki/OpenClaw "OpenClaw")

 |  
 |  
| Applications  | 
  * [Deepfake](https://en.wikipedia.org/wiki/Deepfake "Deepfake")
    * [audio](https://en.wikipedia.org/wiki/Audio_deepfake "Audio deepfake")
  * [Slop](https://en.wikipedia.org/wiki/AI_slop "AI slop")
    * [slopaganda](https://en.wikipedia.org/wiki/Slopaganda "Slopaganda")

 |  
| [Companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies "List of artificial intelligence companies")  | 
  * [Aleph Alpha](https://en.wikipedia.org/wiki/Aleph_Alpha "Aleph Alpha")
  * [Anthropic](https://en.wikipedia.org/wiki/Anthropic "Anthropic")
  * [Anysphere](https://en.wikipedia.org/wiki/Cursor_\(company\) "Cursor \(company\)")
  * [Baichuan](https://en.wikipedia.org/wiki/Baichuan "Baichuan")
  * [Canva](https://en.wikipedia.org/wiki/Canva "Canva")
  * [Cognition AI](https://en.wikipedia.org/wiki/Cognition_AI "Cognition AI")
  * [Cohere](https://en.wikipedia.org/wiki/Cohere "Cohere")
  * [Contextual AI](https://en.wikipedia.org/wiki/Contextual_AI "Contextual AI")
  * [DeepSeek](https://en.wikipedia.org/wiki/DeepSeek "DeepSeek")
  * [DeepL](https://en.wikipedia.org/wiki/DeepL_Translator "DeepL Translator")
  * [EleutherAI](https://en.wikipedia.org/wiki/EleutherAI "EleutherAI")
  * [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs "ElevenLabs")
  * [Google](https://en.wikipedia.org/wiki/Google "Google")
    * [AI](https://en.wikipedia.org/wiki/Google_AI "Google AI")
    * [DeepMind](https://en.wikipedia.org/wiki/Google_DeepMind "Google DeepMind")
  * [HeyGen](https://en.wikipedia.org/wiki/HeyGen "HeyGen")
  * [Hugging Face](https://en.wikipedia.org/wiki/Hugging_Face "Hugging Face")
  * [Inflection AI](https://en.wikipedia.org/wiki/Inflection_AI "Inflection AI")
  * [Kuaishou](https://en.wikipedia.org/wiki/Kuaishou "Kuaishou")
  * [Lightricks](https://en.wikipedia.org/wiki/Lightricks "Lightricks")
  * [Lovable](https://en.wikipedia.org/wiki/Lovable_\(company\) "Lovable \(company\)")
  * [Luma Labs](https://en.wikipedia.org/wiki/Luma_Labs "Luma Labs")
  * [Meta AI](https://en.wikipedia.org/wiki/Meta_AI "Meta AI")
  * [Meta Superintelligence Labs](https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs "Meta Superintelligence Labs")
  * [Microsoft AI](https://en.wikipedia.org/wiki/Microsoft_AI "Microsoft AI")
  * [MiniMax](https://en.wikipedia.org/wiki/MiniMax_Group "MiniMax Group")
  * [Mistral AI](https://en.wikipedia.org/wiki/Mistral_AI "Mistral AI")
  * [Moonshot AI](https://en.wikipedia.org/wiki/Moonshot_AI "Moonshot AI")
  * [OpenAI](https://en.wikipedia.org/wiki/OpenAI "OpenAI")
  * [Perplexity AI](https://en.wikipedia.org/wiki/Perplexity_AI "Perplexity AI")
  * [Runway](https://en.wikipedia.org/wiki/Runway_\(company\) "Runway \(company\)")
  * [Safe Superintelligence](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc. "Safe Superintelligence Inc.")
  * [Sakana AI](https://en.wikipedia.org/wiki/Sakana_AI "Sakana AI")
  * [Salesforce](https://en.wikipedia.org/wiki/Salesforce "Salesforce")
  * [Scale AI](https://en.wikipedia.org/wiki/Scale_AI "Scale AI")
  * [SoundHound AI](https://en.wikipedia.org/wiki/SoundHound_AI "SoundHound AI")
  * [SpaceXAI](https://en.wikipedia.org/wiki/SpaceXAI "SpaceXAI")
  * [Stability AI](https://en.wikipedia.org/wiki/Stability_AI "Stability AI")
  * [StepFun](https://en.wikipedia.org/wiki/StepFun "StepFun")
  * [Synthesia](https://en.wikipedia.org/wiki/Synthesia_\(company\) "Synthesia \(company\)")
  * [Thinking Machines Lab](https://en.wikipedia.org/wiki/Thinking_Machines_Lab "Thinking Machines Lab")
  * [Upstage](https://en.wikipedia.org/wiki/Upstage_\(company\) "Upstage \(company\)")
  * [Xiaomi](https://en.wikipedia.org/wiki/Xiaomi "Xiaomi")
  * [Z.ai](https://en.wikipedia.org/wiki/Z.ai "Z.ai")

 |  
| [Controversies](https://en.wikipedia.org/wiki/Artificial_intelligence_controversies "Artificial intelligence controversies")  | 
  * [Generative AI pornography](https://en.wikipedia.org/wiki/Generative_AI_pornography "Generative AI pornography")
    * [Deepfake pornography](https://en.wikipedia.org/wiki/Deepfake_pornography "Deepfake pornography")
      * [on Grok](https://en.wikipedia.org/wiki/Grok_sexual_deepfake_scandal "Grok sexual deepfake scandal")
      * [of Taylor Swift](https://en.wikipedia.org/wiki/Taylor_Swift_deepfake_pornography_controversy "Taylor Swift deepfake pornography controversy")
  * [Pause Giant AI Experiments](https://en.wikipedia.org/wiki/Pause_Giant_AI_Experiments:_An_Open_Letter "Pause Giant AI Experiments: An Open Letter")
  * [Removal of Sam Altman from OpenAI](https://en.wikipedia.org/wiki/Removal_of_Sam_Altman_from_OpenAI "Removal of Sam Altman from OpenAI")
  * [Statement on AI Risk](https://en.wikipedia.org/wiki/Statement_on_AI_Risk "Statement on AI Risk")
  * [Tay (chatbot)](https://en.wikipedia.org/wiki/Tay_\(chatbot\) "Tay \(chatbot\)")
  * _[Théâtre D'opéra Spatial](https://en.wikipedia.org/wiki/Th%C3%A9%C3%A2tre_D%27op%C3%A9ra_Spatial "Théâtre D'opéra Spatial")_
  * [Voiceverse NFT plagiarism](https://en.wikipedia.org/wiki/Voiceverse_NFT_plagiarism_scandal "Voiceverse NFT plagiarism scandal")

 |  
| 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category](https://en.wikipedia.org/wiki/Category:Generative_AI "Category:Generative AI")
  * [![](https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png)](https://en.wikipedia.org/wiki/File:Commons-logo.svg "Commons page") [Commons](https://commons.wikimedia.org/wiki/Category:Generative_artificial_intelligence "commons:Category:Generative artificial intelligence")

 |  
| 
  * [v](https://en.wikipedia.org/wiki/Template:Artificial_intelligence_navbox "Template:Artificial intelligence navbox")
  * [t](https://en.wikipedia.org/wiki/Template_talk:Artificial_intelligence_navbox "Template talk:Artificial intelligence navbox")
  * [e](https://en.wikipedia.org/wiki/Special:EditPage/Template:Artificial_intelligence_navbox "Special:EditPage/Template:Artificial intelligence navbox")

[Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence "Artificial intelligence") (AI)  |  
| --- |  
| 
  * [History](https://en.wikipedia.org/wiki/History_of_artificial_intelligence "History of artificial intelligence")
    * [timeline](https://en.wikipedia.org/wiki/Timeline_of_artificial_intelligence "Timeline of artificial intelligence")
  * [Glossary](https://en.wikipedia.org/wiki/Glossary_of_artificial_intelligence "Glossary of artificial intelligence")
  * [Companies](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_companies "List of artificial intelligence companies")
  * [Projects](https://en.wikipedia.org/wiki/List_of_artificial_intelligence_projects "List of artificial intelligence projects")
  * [List of open-source AI software](https://en.wikipedia.org/wiki/Lists_of_open-source_artificial_intelligence_software "Lists of open-source artificial intelligence software")

 |  
| Concepts  | 
  * [Automated reasoning](https://en.wikipedia.org/wiki/Automated_reasoning "Automated reasoning")
  * [Parameter](https://en.wikipedia.org/wiki/Parameter "Parameter")
    * [Hyperparameter](https://en.wikipedia.org/wiki/Hyperparameter_\(machine_learning\) "Hyperparameter \(machine learning\)")
  * [Loss functions](https://en.wikipedia.org/wiki/Loss_functions_for_classification "Loss functions for classification")
  * [Regression](https://en.wikipedia.org/wiki/Regression_analysis "Regression analysis")
    * [Bias–variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff "Bias–variance tradeoff")
    * [Double descent](https://en.wikipedia.org/wiki/Double_descent "Double descent")
    * [Overfitting](https://en.wikipedia.org/wiki/Overfitting "Overfitting")
  * [Clustering](https://en.wikipedia.org/wiki/Cluster_analysis "Cluster analysis")
  * [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent "Gradient descent")
    * [SGD](https://en.wikipedia.org/wiki/Stochastic_gradient_descent "Stochastic gradient descent")
    * [Quasi-Newton method](https://en.wikipedia.org/wiki/Quasi-Newton_method "Quasi-Newton method")
    * [Conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method "Conjugate gradient method")
  * [Backpropagation](https://en.wikipedia.org/wiki/Backpropagation "Backpropagation")
  * [Attention](https://en.wikipedia.org/wiki/Attention_\(machine_learning\) "Attention \(machine learning\)")
  * [Convolution](https://en.wikipedia.org/wiki/Convolution "Convolution")
  * [Normalization](https://en.wikipedia.org/wiki/Normalization_\(machine_learning\) "Normalization \(machine learning\)")
    * [Batchnorm](https://en.wikipedia.org/wiki/Batch_normalization "Batch normalization")
  * [Activation](https://en.wikipedia.org/wiki/Activation_function "Activation function")
    * [Softmax](https://en.wikipedia.org/wiki/Softmax_function "Softmax function")
    * [Sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function "Sigmoid function")
    * [Rectifier](https://en.wikipedia.org/wiki/Rectifier_\(neural_networks\) "Rectifier \(neural networks\)")
  * [Gating](https://en.wikipedia.org/wiki/Gating_mechanism "Gating mechanism")
  * [Weight initialization](https://en.wikipedia.org/wiki/Weight_initialization "Weight initialization")
  * [Regularization](https://en.wikipedia.org/wiki/Regularization_\(mathematics\) "Regularization \(mathematics\)")
  * [Datasets](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets "Training, validation, and test data sets")
    * [Augmentation](https://en.wikipedia.org/wiki/Data_augmentation "Data augmentation")
  * [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering "Prompt engineering")
  * [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning "Reinforcement learning")
    * [Q-learning](https://en.wikipedia.org/wiki/Q-learning "Q-learning")
    * [SARSA](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action "State–action–reward–state–action")
    * [Imitation](https://en.wikipedia.org/wiki/Imitation_learning "Imitation learning")
    * [Policy gradient](https://en.wikipedia.org/wiki/Policy_gradient_method "Policy gradient method")
  * [Diffusion](https://en.wikipedia.org/wiki/Diffusion_process "Diffusion process")
  * [Latent diffusion model](https://en.wikipedia.org/wiki/Latent_diffusion_model "Latent diffusion model")
  * [Autoregression](https://en.wikipedia.org/wiki/Autoregressive_model "Autoregressive model")
  * [Adversary](https://en.wikipedia.org/wiki/Adversarial_machine_learning "Adversarial machine learning")
  * RAG
  * [Uncanny valley](https://en.wikipedia.org/wiki/Uncanny_valley "Uncanny valley")
  * [RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback "Reinforcement learning from human feedback")
  * [Self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning "Self-supervised learning")
  * [Reflection](https://en.wikipedia.org/wiki/Reflection_\(artificial_intelligence\) "Reflection \(artificial intelligence\)")
  * [Recursive self-improvement](https://en.wikipedia.org/wiki/Recursive_self-improvement "Recursive self-improvement")
  * [Hallucination](https://en.wikipedia.org/wiki/Hallucination_\(artificial_intelligence\) "Hallucination \(artificial intelligence\)")
  * [Word embedding](https://en.wikipedia.org/wiki/Word_embedding "Word embedding")
  * [Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding "Vibe coding")
  * [Symbolic AI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence "Symbolic artificial intelligence")

 |  
| [Applications](https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence "Applications of artificial intelligence")  | 
  * [Automated theorem proving](https://en.wikipedia.org/wiki/Automated_theorem_proving "Automated theorem proving")
  * [Machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning")
    * [In-context learning](https://en.wikipedia.org/wiki/Prompt_engineering#In-context_learning "Prompt engineering")
  * [Artificial neural network](https://en.wikipedia.org/wiki/Neural_network_\(machine_learning\) "Neural network \(machine learning\)")
    * [Deep learning](https://en.wikipedia.org/wiki/Deep_learning "Deep learning")
  * [Language model](https://en.wikipedia.org/wiki/Language_model "Language model")
    * [Large](https://en.wikipedia.org/wiki/Large_language_model "Large language model")
    * [NMT](https://en.wikipedia.org/wiki/Neural_machine_translation "Neural machine translation")
    * [Reasoning](https://en.wikipedia.org/wiki/Reasoning_model "Reasoning model")
  * [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol "Model Context Protocol")
  * [Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent "Intelligent agent")
    * [AI agent](https://en.wikipedia.org/wiki/AI_agent "AI agent")
  * [Artificial human companion](https://en.wikipedia.org/wiki/Artificial_human_companion "Artificial human companion")
  * [Humanity's Last Exam](https://en.wikipedia.org/wiki/Humanity%27s_Last_Exam "Humanity's Last Exam")
  * [Lethal autonomous weapons (LAWs)](https://en.wikipedia.org/wiki/Lethal_autonomous_weapon "Lethal autonomous weapon")
  * [Generative AI](https://en.wikipedia.org/wiki/Generative_AI "Generative AI")
  * [Weak AI](https://en.wikipedia.org/wiki/Weak_artificial_intelligence "Weak artificial intelligence")
  * Hypothetical 
    * [Artificial general intelligence (AGI)](https://en.wikipedia.org/wiki/Artificial_general_intelligence "Artificial general intelligence")
    * [Artificial superintelligence (ASI)](https://en.wikipedia.org/wiki/Artificial_superintelligence "Artificial superintelligence")
  * [Agent2Agent protocol](https://en.wikipedia.org/wiki/Agent2Agent "Agent2Agent")

 |  
| Implementations  |   
 | Audio–visual  | 
  * [AlexNet](https://en.wikipedia.org/wiki/AlexNet "AlexNet")
  * [WaveNet](https://en.wikipedia.org/wiki/WaveNet "WaveNet")
  * [Human image synthesis](https://en.wikipedia.org/wiki/Human_image_synthesis "Human image synthesis")
  * [HWR](https://en.wikipedia.org/wiki/Handwriting_recognition "Handwriting recognition")
  * [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition "Optical character recognition")
  * [Computer vision](https://en.wikipedia.org/wiki/Computer_vision "Computer vision")
  * [Speech synthesis](https://en.wikipedia.org/wiki/Deep_learning_speech_synthesis "Deep learning speech synthesis")
    * [15.ai](https://en.wikipedia.org/wiki/15.ai "15.ai")
    * [ElevenLabs](https://en.wikipedia.org/wiki/ElevenLabs "ElevenLabs")
  * [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition "Speech recognition")
    * [Whisper](https://en.wikipedia.org/wiki/Whisper_\(speech_recognition_system\) "Whisper \(speech recognition system\)")
  * [Facial recognition](https://en.wikipedia.org/wiki/Facial_recognition_system "Facial recognition system")
  * [AlphaFold](https://en.wikipedia.org/wiki/AlphaFold "AlphaFold")
  * [Text-to-image models](https://en.wikipedia.org/wiki/Text-to-image_model "Text-to-image model")
    * [Aurora](https://en.wikipedia.org/wiki/Aurora_\(text-to-image_model\) "Aurora \(text-to-image model\)")
    * [DALL-E](https://en.wikipedia.org/wiki/DALL-E "DALL-E")
    * [Firefly](https://en.wikipedia.org/wiki/Adobe_Firefly "Adobe Firefly")
    * [Flux](https://en.wikipedia.org/wiki/Flux_\(text-to-image_model\) "Flux \(text-to-image model\)")
    * [GPT Image](https://en.wikipedia.org/wiki/GPT_Image "GPT Image")
    * [Ideogram](https://en.wikipedia.org/wiki/Ideogram_\(text-to-image_model\) "Ideogram \(text-to-image model\)")
    * [Imagen](https://en.wikipedia.org/wiki/Imagen_\(text-to-image_model\) "Imagen \(text-to-image model\)")
    * [Midjourney](https://en.wikipedia.org/wiki/Midjourney "Midjourney")
    * [Recraft](https://en.wikipedia.org/wiki/Recraft "Recraft")
    * [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion "Stable Diffusion")
  * [Text-to-video models](https://en.wikipedia.org/wiki/Text-to-video_model "Text-to-video model")
    * [Dream Machine](https://en.wikipedia.org/wiki/Dream_Machine_\(text-to-video_model\) "Dream Machine \(text-to-video model\)")
    * [Runway Gen](https://en.wikipedia.org/wiki/Runway_\(company\)#Services_and_technologies "Runway \(company\)")
    * [Hailuo AI](https://en.wikipedia.org/wiki/MiniMax_\(company\)#Hailuo_AI "MiniMax \(company\)")
    * [Kling](https://en.wikipedia.org/wiki/Kling_AI "Kling AI")
    * [Sora](https://en.wikipedia.org/wiki/Sora_\(text-to-video_model\) "Sora \(text-to-video model\)")
    * [Seedance](https://en.wikipedia.org/wiki/Seedance_2.0 "Seedance 2.0")
    * [Veo](https://en.wikipedia.org/wiki/Veo_\(text-to-video_model\) "Veo \(text-to-video model\)")
  * [Music generation](https://en.wikipedia.org/wiki/Artificial_intelligence_in_music "Artificial intelligence in music")
    * [Riffusion](https://en.wikipedia.org/wiki/Riffusion "Riffusion")
    * [Suno](https://en.wikipedia.org/wiki/Suno_\(platform\) "Suno \(platform\)")
    * [Udio](https://en.wikipedia.org/wiki/Udio "Udio")
  * [World models](https://en.wikipedia.org/wiki/World_model_\(artificial_intelligence\) "World model \(artificial intelligence\)")
    * [Genie](https://en.wikipedia.org/wiki/Genie_\(world_model\) "Genie \(world model\)")
    * [_Oasis_](https://en.wikipedia.org/wiki/Oasis_\(Minecraft_clone\) "Oasis \(Minecraft clone\)")

 |  
| --- | --- |  
| Text  | 
  * [List of large language models](https://en.wikipedia.org/wiki/List_of_large_language_models "List of large language models")
  * [Project Debater](https://en.wikipedia.org/wiki/Project_Debater "Project Debater")
  * [IBM Watson](https://en.wikipedia.org/wiki/IBM_Watson "IBM Watson")
    * [IBM Watsonx](https://en.wikipedia.org/wiki/IBM_Watsonx "IBM Watsonx")

 |  
| Decisional  | 
  * [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo "AlphaGo")
  * [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero "AlphaZero")
  * [OpenAI Five](https://en.wikipedia.org/wiki/OpenAI_Five "OpenAI Five")
  * [Self-driving car](https://en.wikipedia.org/wiki/Self-driving_car "Self-driving car")
  * [MuZero](https://en.wikipedia.org/wiki/MuZero "MuZero")
  * [Action selection](https://en.wikipedia.org/wiki/Action_selection "Action selection")
    * [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT "AutoGPT")
  * [Robot control](https://en.wikipedia.org/wiki/Robot_control "Robot control")

 |  
| [Reasoning systems](https://en.wikipedia.org/wiki/Reasoning_system "Reasoning system")  | 
  * [Deductive classifiers](https://en.wikipedia.org/wiki/Deductive_classifier "Deductive classifier")
  * [Expert systems](https://en.wikipedia.org/wiki/Expert_system "Expert system")
  * [Inference engines](https://en.wikipedia.org/wiki/Inference_engine "Inference engine")
  * [Knowledge-based systems](https://en.wikipedia.org/wiki/Knowledge-based_system "Knowledge-based system")
  * [Logic programs](https://en.wikipedia.org/wiki/Logic_program "Logic program")
  * [Procedural reasoning systems](https://en.wikipedia.org/wiki/Procedural_reasoning_system "Procedural reasoning system")
  * [Semantic reasoners](https://en.wikipedia.org/wiki/Semantic_reasoner "Semantic reasoner")
  * [Rule-based systems](https://en.wikipedia.org/wiki/Rule-based_system "Rule-based system")

 |  
 |  
| People  | 
  * [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing "Alan Turing")
  * [Warren Sturgis McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch "Warren Sturgis McCulloch")
  * [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts "Walter Pitts")
  * [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann "John von Neumann")
  * [Christopher D. Manning](https://en.wikipedia.org/wiki/Christopher_D._Manning "Christopher D. Manning")
  * [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon "Claude Shannon")
  * [Shun'ichi Amari](https://en.wikipedia.org/wiki/Shun%27ichi_Amari "Shun'ichi Amari")
  * [Kunihiko Fukushima](https://en.wikipedia.org/wiki/Kunihiko_Fukushima "Kunihiko Fukushima")
  * [Takeo Kanade](https://en.wikipedia.org/wiki/Takeo_Kanade "Takeo Kanade")
  * [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky "Marvin Minsky")
  * [John McCarthy](https://en.wikipedia.org/wiki/John_McCarthy_\(computer_scientist\) "John McCarthy \(computer scientist\)")
  * [Nathaniel Rochester](https://en.wikipedia.org/wiki/Nathaniel_Rochester_\(computer_scientist\) "Nathaniel Rochester \(computer scientist\)")
  * [Allen Newell](https://en.wikipedia.org/wiki/Allen_Newell "Allen Newell")
  * [Cliff Shaw](https://en.wikipedia.org/wiki/Cliff_Shaw "Cliff Shaw")
  * [Herbert A. Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon "Herbert A. Simon")
  * [Oliver Selfridge](https://en.wikipedia.org/wiki/Oliver_Selfridge "Oliver Selfridge")
  * [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt "Frank Rosenblatt")
  * [Bernard Widrow](https://en.wikipedia.org/wiki/Bernard_Widrow "Bernard Widrow")
  * [Joseph Weizenbaum](https://en.wikipedia.org/wiki/Joseph_Weizenbaum "Joseph Weizenbaum")
  * [Seymour Papert](https://en.wikipedia.org/wiki/Seymour_Papert "Seymour Papert")
  * [Seppo Linnainmaa](https://en.wikipedia.org/wiki/Seppo_Linnainmaa "Seppo Linnainmaa")
  * [Paul Werbos](https://en.wikipedia.org/wiki/Paul_Werbos "Paul Werbos")
  * [Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton "Geoffrey Hinton")
  * [John Hopfield](https://en.wikipedia.org/wiki/John_Hopfield "John Hopfield")
  * [Jürgen Schmidhuber](https://en.wikipedia.org/wiki/J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")
  * [Yann LeCun](https://en.wikipedia.org/wiki/Yann_LeCun "Yann LeCun")
  * [Yoshua Bengio](https://en.wikipedia.org/wiki/Yoshua_Bengio "Yoshua Bengio")
  * [Lotfi A. Zadeh](https://en.wikipedia.org/wiki/Lotfi_A._Zadeh "Lotfi A. Zadeh")
  * [Stephen Grossberg](https://en.wikipedia.org/wiki/Stephen_Grossberg "Stephen Grossberg")
  * [Alex Graves](https://en.wikipedia.org/wiki/Alex_Graves_\(computer_scientist\) "Alex Graves \(computer scientist\)")
  * [James Goodnight](https://en.wikipedia.org/wiki/James_Goodnight "James Goodnight")
  * [Andrew Ng](https://en.wikipedia.org/wiki/Andrew_Ng "Andrew Ng")
  * [Fei-Fei Li](https://en.wikipedia.org/wiki/Fei-Fei_Li "Fei-Fei Li")
  * [Alex Krizhevsky](https://en.wikipedia.org/wiki/Alex_Krizhevsky "Alex Krizhevsky")
  * [Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever "Ilya Sutskever")
  * [Oriol Vinyals](https://en.wikipedia.org/wiki/Oriol_Vinyals "Oriol Vinyals")
  * [Quoc V. Le](https://en.wikipedia.org/wiki/Quoc_V._Le "Quoc V. Le")
  * [Ian Goodfellow](https://en.wikipedia.org/wiki/Ian_Goodfellow "Ian Goodfellow")
  * [Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis "Demis Hassabis")
  * [David Silver](https://en.wikipedia.org/wiki/David_Silver_\(computer_scientist\) "David Silver \(computer scientist\)")
  * [Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy "Andrej Karpathy")
  * [Ashish Vaswani](https://en.wikipedia.org/wiki/Ashish_Vaswani "Ashish Vaswani")
  * [Noam Shazeer](https://en.wikipedia.org/wiki/Noam_Shazeer "Noam Shazeer")
  * [Aidan Gomez](https://en.wikipedia.org/wiki/Aidan_Gomez "Aidan Gomez")
  * [John Schulman](https://en.wikipedia.org/wiki/John_Schulman "John Schulman")
  * [Mustafa Suleyman](https://en.wikipedia.org/wiki/Mustafa_Suleyman "Mustafa Suleyman")
  * [Jan Leike](https://en.wikipedia.org/wiki/Jan_Leike "Jan Leike")
  * [Daniel Kokotajlo](https://en.wikipedia.org/wiki/Daniel_Kokotajlo_\(researcher\) "Daniel Kokotajlo \(researcher\)")
  * [François Chollet](https://en.wikipedia.org/wiki/Fran%C3%A7ois_Chollet "François Chollet")

 |  
| Architectures  | 
  * [Neural Turing machine](https://en.wikipedia.org/wiki/Neural_Turing_machine "Neural Turing machine")
  * [Differentiable neural computer](https://en.wikipedia.org/wiki/Differentiable_neural_computer "Differentiable neural computer")
  * [Transformer](https://en.wikipedia.org/wiki/Transformer_\(deep_learning\) "Transformer \(deep learning\)")
    * [Vision transformer (ViT)](https://en.wikipedia.org/wiki/Vision_transformer "Vision transformer")
  * [Recurrent neural network (RNN)](https://en.wikipedia.org/wiki/Recurrent_neural_network "Recurrent neural network")
  * [Long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory "Long short-term memory")
  * [Gated recurrent unit (GRU)](https://en.wikipedia.org/wiki/Gated_recurrent_unit "Gated recurrent unit")
  * [Echo state network](https://en.wikipedia.org/wiki/Echo_state_network "Echo state network")
  * [Multilayer perceptron (MLP)](https://en.wikipedia.org/wiki/Multilayer_perceptron "Multilayer perceptron")
  * [Convolutional neural network (CNN)](https://en.wikipedia.org/wiki/Convolutional_neural_network "Convolutional neural network")
  * [Residual neural network (RNN)](https://en.wikipedia.org/wiki/Residual_neural_network "Residual neural network")
  * [Highway network](https://en.wikipedia.org/wiki/Highway_network "Highway network")
  * [Mamba](https://en.wikipedia.org/wiki/Mamba_\(deep_learning_architecture\) "Mamba \(deep learning architecture\)")
  * [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder "Autoencoder")
  * [Variational autoencoder (VAE)](https://en.wikipedia.org/wiki/Variational_autoencoder "Variational autoencoder")
  * [Generative adversarial network (GAN)](https://en.wikipedia.org/wiki/Generative_adversarial_network "Generative adversarial network")
  * [Graph neural network (GNN)](https://en.wikipedia.org/wiki/Graph_neural_network "Graph neural network")

 |  
| Political  | 
  * [AI Cold War](https://en.wikipedia.org/wiki/Artificial_Intelligence_Cold_War "Artificial Intelligence Cold War")
  * [AI safety](https://en.wikipedia.org/wiki/AI_safety "AI safety") ([Alignment](https://en.wikipedia.org/wiki/AI_alignment "AI alignment"))
  * [AI takeover](https://en.wikipedia.org/wiki/AI_takeover "AI takeover")
  * [Elections](https://en.wikipedia.org/wiki/Artificial_intelligence_and_elections "Artificial intelligence and elections")
  * [Ethics of AI](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence "Ethics of artificial intelligence")
  * EU [AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act "Artificial Intelligence Act")
  * [Nationalism](https://en.wikipedia.org/wiki/AI_nationalism "AI nationalism")
  * [Precautionary principle](https://en.wikipedia.org/wiki/Precautionary_principle "Precautionary principle")
  * [Regulation of AI](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence "Regulation of artificial intelligence")
    * [US](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence_in_the_United_States "Regulation of artificial intelligence in the United States")
  * [Virtual politician](https://en.wikipedia.org/wiki/Virtual_politician "Virtual politician")

 |  
| Social and economic  | 
  * [AI boom](https://en.wikipedia.org/wiki/AI_boom "AI boom")
  * [AI bubble](https://en.wikipedia.org/wiki/AI_bubble "AI bubble")
  * [AI data center](https://en.wikipedia.org/wiki/AI_data_center "AI data center")
  * [AI effect](https://en.wikipedia.org/wiki/AI_effect "AI effect")
  * [AI literacy](https://en.wikipedia.org/wiki/AI_literacy "AI literacy")
  * [AI slop](https://en.wikipedia.org/wiki/AI_slop "AI slop")
  * [AI veganism](https://en.wikipedia.org/wiki/AI_veganism "AI veganism")
  * [AI winter](https://en.wikipedia.org/wiki/AI_winter "AI winter")
  * [Anthropomorphism](https://en.wikipedia.org/wiki/AI_anthropomorphism "AI anthropomorphism")
  * [Arms race](https://en.wikipedia.org/wiki/Artificial_intelligence_arms_race "Artificial intelligence arms race")
  * [Competition](https://en.wikipedia.org/wiki/Competition_in_artificial_intelligence "Competition in artificial intelligence")
  * [Environmental impact](https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence "Environmental impact of artificial intelligence")
  * [Explainable AI](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence "Explainable artificial intelligence")
  * [Generative engine optimization](https://en.wikipedia.org/wiki/Generative_engine_optimization "Generative engine optimization")
  * [In architecture](https://en.wikipedia.org/wiki/Artificial_intelligence_in_architecture "Artificial intelligence in architecture")
  * [In education](https://en.wikipedia.org/wiki/Artificial_intelligence_in_education "Artificial intelligence in education")
  * [In fiction](https://en.wikipedia.org/wiki/Artificial_intelligence_in_fiction "Artificial intelligence in fiction")
  * [In healthcare](https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare "Artificial intelligence in healthcare")
    * [Chatbot psychosis](https://en.wikipedia.org/wiki/Chatbot_psychosis "Chatbot psychosis")
  * [In marketing](https://en.wikipedia.org/wiki/Artificial_intelligence_in_marketing "Artificial intelligence in marketing")
  * [In video games](https://en.wikipedia.org/wiki/Artificial_intelligence_in_video_games "Artificial intelligence in video games")
  * [In visual art](https://en.wikipedia.org/wiki/Artificial_intelligence_visual_art "Artificial intelligence visual art")
  * [Military applications](https://en.wikipedia.org/wiki/Military_applications_of_artificial_intelligence "Military applications of artificial intelligence")
    * [AI warfare](https://en.wikipedia.org/wiki/AI_warfare "AI warfare")
  * [Workplace impact](https://en.wikipedia.org/wiki/Workplace_impact_of_artificial_intelligence "Workplace impact of artificial intelligence")

 |  
| 
  * ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png) [Category](https://en.wikipedia.org/wiki/Category:Artificial_intelligence "Category:Artificial intelligence")

 |  
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&oldid=1357460039](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&oldid=1357460039)"
[Categories](https://en.wikipedia.org/wiki/Help:Category "Help:Category"): 
  * [Large language models](https://en.wikipedia.org/wiki/Category:Large_language_models "Category:Large language models")
  * [Natural language processing](https://en.wikipedia.org/wiki/Category:Natural_language_processing "Category:Natural language processing")
  * [Information retrieval systems](https://en.wikipedia.org/wiki/Category:Information_retrieval_systems "Category:Information retrieval systems")
  * [Generative AI](https://en.wikipedia.org/wiki/Category:Generative_AI "Category:Generative AI")


Hidden categories: 
  * [Articles with short description](https://en.wikipedia.org/wiki/Category:Articles_with_short_description "Category:Articles with short description")
  * [Short description is different from Wikidata](https://en.wikipedia.org/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
  * [Articles containing potentially dated statements from 2023](https://en.wikipedia.org/wiki/Category:Articles_containing_potentially_dated_statements_from_2023 "Category:Articles containing potentially dated statements from 2023")
  * [All articles containing potentially dated statements](https://en.wikipedia.org/wiki/Category:All_articles_containing_potentially_dated_statements "Category:All articles containing potentially dated statements")
  * [All articles with unsourced statements](https://en.wikipedia.org/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
  * [Articles with unsourced statements from June 2026](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_June_2026 "Category:Articles with unsourced statements from June 2026")
  * [Articles with unsourced statements from August 2025](https://en.wikipedia.org/wiki/Category:Articles_with_unsourced_statements_from_August_2025 "Category:Articles with unsourced statements from August 2025")


  * This page was last edited on 2 June 2026, at 20:06 (UTC).
  * Text is available under the [Creative Commons Attribution-ShareAlike 4.0 License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License "Wikipedia:Text of the Creative Commons Attribution-ShareAlike 4.0 International License"); additional terms may apply. By using this site, you agree to the [Terms of Use](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use "foundation:Special:MyLanguage/Policy:Terms of Use") and [Privacy Policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy "foundation:Special:MyLanguage/Policy:Privacy policy"). Wikipedia® is a registered trademark of the [Wikimedia Foundation, Inc.](https://wikimediafoundation.org/), a non-profit organization.


  * [Privacy policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy)
  * [About Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:About)
  * [Disclaimers](https://en.wikipedia.org/wiki/Wikipedia:General_disclaimer)
  * [Contact Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Contact_us)
  * [Legal & safety contacts](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Legal:Wikimedia_Foundation_Legal_and_Safety_Contact_Information)
  * [Code of Conduct](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct)
  * [Developers](https://developer.wikimedia.org)
  * [Statistics](https://stats.wikimedia.org/#/en.wikipedia.org)
  * [Cookie statement](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement)
  * [Mobile view](https://en.wikipedia.org/w/index.php?title=Retrieval-augmented_generation&mobileaction=toggle_view_mobile)


  * [![Wikimedia Foundation](https://en.wikipedia.org/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
  * [![Powered by MediaWiki](https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)


Search
Search
Toggle the table of contents
Retrieval-augmented generation
[](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) [](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
21 languages [Add topic ](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
  *[v]: View this template
  *[t]: Discuss this template
  *[e]: Edit this template
